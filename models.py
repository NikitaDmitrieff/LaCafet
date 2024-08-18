from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import CheckConstraint, DateTime
from sqlalchemy import Column, Integer, LargeBinary
from wtforms import IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError

db = SQLAlchemy()


class GuidanceCounselorModel(db.Model):
    __tablename__ = "guidance_counselor"

    id = Column(Integer, primary_key=True)
    vector_store = Column(LargeBinary, nullable=False)


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text_entry = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, index=True, unique=False)
    from_human = db.Column(db.Boolean, nullable=False, default=False)

    conversation_id = db.Column(
        db.Integer, db.ForeignKey("conversation.id"), nullable=False
    )

    def __repr__(self):
        return f"<Entry {self.id}: {self.text_entry}>"


class Conversation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    entries = db.relationship("Entry", backref="conversation", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    classification = db.Column(db.String(30), nullable=True)
    start_date = db.Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Entry {self.id}: {self.entries}>"


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    conversations = db.relationship("Conversation", backref="user", lazy=True)
    age = db.Column(db.Integer, nullable=False, info={"min": 7, "max": 99})
    vector_store = db.Column(LargeBinary, nullable=True)

    __table_args__ = (
        CheckConstraint(age >= 1, name="check_age_lower_bound"),
        CheckConstraint(age <= 99, name="check_age_upper_bound"),
    )


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=20)],
        render_kw={"placeholder": "Username"},
    )

    password = PasswordField(
        validators=[InputRequired(), Length(min=1, max=20)],
        render_kw={"placeholder": "Password"},
    )

    age = IntegerField(
        validators=[InputRequired(), NumberRange(min=1, max=99)],
        render_kw={"placeholder": "Age"},
    )

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one."
            )


class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=4, max=20)],
        render_kw={"placeholder": "Username"},
    )

    password = PasswordField(
        validators=[InputRequired(), Length(min=1, max=20)],
        render_kw={"placeholder": "Password"},
    )

    submit = SubmitField("Login")
