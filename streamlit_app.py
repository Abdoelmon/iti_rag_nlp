import streamlit as st
import requests
import time

st.set_page_config(page_title="RAG NLP System", layout="wide")

st.title("🧠 RAG NLP System with PDF Chat & Summary")

with st.sidebar:
    st.header("📂 PDF Controls")

    user_id = st.text_input("Enter User ID").lower()
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    
    if uploaded_file and st.button("Upload PDF"):
        files = {"file": uploaded_file.getvalue()}
        data = {"user_id": user_id}
        try:
            r = requests.post("http://localhost:8000/upload", files=files, data=data)
            if r.status_code == 200:
                st.success("PDF Uploaded & Indexed Successfully ✅")
            else:
                st.error(f"Upload failed: {r.json().get('detail', r.text)}")
        except Exception as e:
            st.error(f"Upload error: {e}")

    
    if uploaded_file and st.button("Summarize PDF"):
        try:
            r = requests.post(
                "http://localhost:8000/summarize",
                data={"user_id": user_id}
            )
            if r.status_code == 200:
                summary = r.json().get("summary", "")
                st.subheader("📝 PDF Summary")
                st.markdown(summary)   
            else:
                st.error(f"Summarize failed: {r.json().get('detail', r.text)}")
        except Exception as e:
            st.error(f"Summarize error: {e}")



if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def stream_text(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.03)  


question = st.chat_input("Ask something about the PDF...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    try:
        r = requests.post(
            "http://localhost:8000/ask",
            params={"user_id": user_id, "question": question}
        )

        if r.status_code == 200:
            answer = r.json().get("answer", "")

            with st.chat_message("assistant"):
                placeholder = st.empty()   
                buffer_text = ""           

                
                for chunk in stream_text(answer):
                    buffer_text += chunk
                    placeholder.write(buffer_text)   

                
                placeholder.markdown(answer)          

            
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        else:
            st.error(f"Ask failed: {r.json().get('detail', r.text)}")

    except Exception as e:
        st.error(f"Ask error: {e}")