import requests
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Rohan's AI Assistant",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded" # This forces it open
)

# 2. Load CSS
with open("ui/styles.css", encoding="utf-8") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# 3. Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

# 4. Sidebar
with st.sidebar:
    st.markdown("## 💬 Conversations")
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 📎 Documents")
    # File Uploader in sidebar as a consistent attachment point
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    st.markdown("---")
    st.markdown("### History")
    for idx, title in enumerate(reversed(st.session_state.history)):
        st.button(title, key=f"hist_{idx}", use_container_width=True)

# 5. Main Content
st.markdown("<h1 style='text-align: center;'>🤖 Rohan's AI Assistant</h1>", unsafe_allow_html=True)

# Display Messages
for message in st.session_state.messages:
    # 'is_user' parameter ensures native Streamlit alignment (right for user, left for bot)
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input
if prompt := st.chat_input("Message AI Assistant..."):
    # Add to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # API Call
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:8000/chat",
                    json={"message": prompt, "chat_history": st.session_state.messages},
                    timeout=120
                )
                result = response.json()
                assistant_response = result.get("response", "Error: No response.")
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                st.error(f"Backend Error: {str(e)}")