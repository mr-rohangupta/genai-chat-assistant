import requests
import streamlit as st

APP_NAME = "Rohan's Chat Assistant"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide"
)

# ======================
# Load CSS
# ======================

with open(
        "ui/styles.css",
        encoding="utf-8"
) as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ======================
# Session State
# ======================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

# ======================
# Sidebar
# ======================

with st.sidebar:

    if st.button(
            "➕ New Chat",
            use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    uploaded_pdf = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

    st.markdown("### 💬 Chats")
    st.markdown("---")

    if not st.session_state.history:

        st.caption(
            "No conversations"
        )

    else:

        for index, title in enumerate(
                reversed(st.session_state.history)
        ):

            st.button(
                title,
                key=f"history_{index}",
                use_container_width=True
            )

# ======================
# PDF Upload
# ======================

if uploaded_pdf:

    try:

        files = {
            "file": (
                uploaded_pdf.name,
                uploaded_pdf.getvalue(),
                "application/pdf"
            )
        }

        response = requests.post(
            "http://localhost:8000/upload-pdf",
            files=files,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        st.success(
            f"✅ {result['file_name']} uploaded successfully"
        )

        st.info(
            f"Characters Extracted: {result['characters']}"
        )

        st.info(
            f"Chunks Created: {result['chunks']}"
        )

    except Exception as e:

        st.error(
            f"Upload Error: {str(e)}"
        )

# ======================
# Welcome Screen
# ======================

if len(st.session_state.messages) == 0:

    st.markdown(
        "<br><br><br>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(
        [1, 3, 1]
    )

    with col2:

        st.title(
            "🤖 Rohan's AI Assistant"
        )

        st.caption(
            "Conversational RAG • Memory • PDF RAG"
        )

# ======================
# Chat Messages
# ======================

for message in st.session_state.messages:

    with st.chat_message(
            message["role"]
    ):

        st.write(
            message["content"]
        )

# ======================
# Chat Input
# ======================

user_input = st.chat_input(
    "Message AI Assistant..."
)

if user_input:

    if len(st.session_state.messages) == 0:

        st.session_state.history.append(
            user_input[:50]
        )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        with st.spinner(
                "Thinking..."
        ):

            response = requests.post(
                "http://localhost:8000/chat",
                json={
                    "message": user_input,
                    "chat_history": st.session_state.messages
                },
                timeout=120
            )

            response.raise_for_status()

            result = response.json()

            assistant_response = (
                result["response"]
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_response
                }
            )

            st.rerun()

    except Exception as e:

        st.error(
            f"Backend Error: {str(e)}"
        )