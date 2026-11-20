import streamlit as st
from rag_pipeline import ask_medical_ai

# Page configuration
st.set_page_config(
    page_title="Cancer Medical AI Agent",
    page_icon="🎗️",
    layout="wide"
)

# Custom title
st.title("🎗️ Cancer Medical AI Agent")

st.write(
    "AI chatbot using Retrieval-Augmented Generation (RAG) "
    "for cancer-related educational information."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask a cancer-related question...")

if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching cancer PDF knowledge base..."):

            try:
                answer = ask_medical_ai(question)

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                error_message = f"Error: {str(e)}"

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })