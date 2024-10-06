import streamlit as st

from backend.app.comet_helper.main import GuidanceCounselor

# Page and Sidebar titles
st.sidebar.markdown("# Comet Helper page 🎈")


# Initialize GuidanceCounselor
if "guidance_counselor" not in st.session_state:
    st.title("Comet Helper Bot")
    st.session_state.guidance_counselor = guidance_counselor = GuidanceCounselor()
else:
    st.title("Comet Helper Bot ✔️")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.checkbox("Display HTML?"):
    display_html = False
else:
    display_html = True

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if not display_html:
            st.markdown(message["content"], unsafe_allow_html=True)
        else:
            st.markdown(message["content"])


prompt = st.chat_input("Ask any question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt, unsafe_allow_html=True)

    answer, _, _ = st.session_state.guidance_counselor.generate_answer(
        user_question=prompt
    )

    # Add assistant message to session state and display it
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
