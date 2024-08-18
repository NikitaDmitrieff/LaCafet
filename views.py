import os

from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import login_required, login_user, logout_user
from langchain_community.vectorstores import FAISS

from backend.chat_utils import load_embedding
from backend.main import GuidanceCounselor
from instances_generator import bcrypt, login_manager
from models import Conversation, Entry, LoginForm, RegisterForm, User, db

script_dir = os.path.dirname(os.path.abspath(__file__))

bp = Blueprint("Comet", __name__)
messages = []


class Message:
    def __init__(self, text, user=True):
        self.text = text
        self.user = user


@bp.route("/login", methods=["GET", "POST"])
@login_manager.user_loader
def login():
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                session["logged_in"] = True
                session["user_id"] = user.id
                session["username"] = username
                session["age"] = user.age
                return redirect(url_for("Comet.index"))

    return render_template("login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        username = form.username.data
        age = form.age.data
        new_user = User(username=username, password=hashed_password, age=age)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        session["logged_in"] = True
        session["user_id"] = new_user.id
        session["username"] = username
        session["age"] = new_user.age

        return redirect(url_for("Comet.index"))

    return render_template("signup.html", form=form)


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "POST":

        try:
            embeddings = load_embedding()

            vector_store = FAISS.load_local(
                "./vector_store/faiss_index",
                embeddings,
                allow_dangerous_deserialization=True,
            )

            guidance_counselor = GuidanceCounselor(
                pdf_directory="/Users/nikita.dmitrieff/Desktop/Personal/Comet/data",
            )

            guidance_counselor.vector_store = vector_store

        except:

            # 1. Create a guidance_counselor instance
            guidance_counselor = GuidanceCounselor(
                pdf_directory="/Users/nikita.dmitrieff/Desktop/Personal/Comet/data",
            )

            # 2. Create vector store
            guidance_counselor.ingest_pdfs_to_vector_store()

            # 3. Save vector store
            guidance_counselor.vector_store.save_local("./vector_store/faiss_index")

        # Retrieve message
        user_question = request.form["message"]
        user_message = Message(user_question, True)

        if not session.get("not_first_prompt"):
            session["not_first_prompt"] = True
            first_prompt = True
        else:
            first_prompt = False

        print(f"generating answer with {first_prompt=}, {user_question=}")

        bot_answer = generate_answer(
            user_question=user_question, guidance_counselor=guidance_counselor
        )
        bot_message = Message(bot_answer, False)

        # Add messages
        messages.append(user_message)
        messages.append(bot_message)

        add_exchange(user_question, bot_answer, exchange_type="History")

    return render_template("index.html", messages=messages)


def generate_answer(
    user_question: str = "Combien d'écoles après le bac ?",
    guidance_counselor: GuidanceCounselor = None,
):
    answer, system_prompt, user_prompt = guidance_counselor.generate_answer(
        user_question=user_question
    )

    print(system_prompt)
    print(user_prompt)

    return answer


def add_exchange(message: str, answer: str, exchange_type: str = "History"):

    user_id = session.get("user_id")
    # username = session.get("username")

    if not session.get("current_conversation_id"):
        current_conversation = Conversation(
            user_id=user_id, classification=exchange_type
        )
        db.session.add(current_conversation)
        db.session.commit()
        session["current_conversation_id"] = current_conversation.id

        # Add to DB
        new_entry_human = Entry(
            text_entry=message,
            user_id=user_id,
            from_human=True,
            conversation_id=current_conversation.id,
        )

        new_entry_bot = Entry(
            text_entry=answer,
            user_id=user_id,
            from_human=False,
            conversation_id=current_conversation.id,
        )

    else:
        current_conversation_id = session["current_conversation_id"]
        # Add to DB
        new_entry_human = Entry(
            text_entry=message,
            user_id=user_id,
            from_human=True,
            conversation_id=current_conversation_id,
        )
        new_entry_bot = Entry(
            text_entry=answer,
            user_id=user_id,
            from_human=False,
            conversation_id=current_conversation_id,
        )

    db.session.add(new_entry_human)
    db.session.add(new_entry_bot)

    db.session.commit()


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("Comet.login"))
