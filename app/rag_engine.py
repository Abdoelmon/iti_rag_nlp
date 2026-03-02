import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class RAGEngine:

    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_template("""
        Answer based only on the context.

        Context:
        {context}

        Question:
        {question}
        """)

        self.parser = StrOutputParser()
    
    def ask(self, question: str, user_id: str):
        index_path = f"storage/indexes/{user_id}"
        
        if not os.path.exists(index_path):
            raise Exception("No index found for this user. Please upload a PDF first.")

        vectorstore = FAISS.load_local(
            index_path,
            self.embedding,
            allow_dangerous_deserialization=True
        )

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4}
        )

        docs = retriever.invoke(question)
        context = "\n\n".join([d.page_content for d in docs])

        chain = self.prompt | self.llm | self.parser

        return chain.invoke({
            "context": context,
            "question": question
        })
    def ask_with_memory(self, question: str, user_id: str, history_length=5):
        index_path = f"storage/indexes/{user_id}"
        if not os.path.exists(index_path):
            raise Exception("No index found for this user.")

        vectorstore = FAISS.load_local(index_path, self.embedding)

        
        history = self.db.get_last_messages(user_id, limit=history_length)
        history_context = "\n".join([f"Q: {h['question']}\nA: {h['answer']}" for h in history])

        
        docs = vectorstore.similarity_search(question, k=4)
        context = "\n".join([d.page_content for d in docs])

        
        prompt = f"Context from PDF:\n{context}\n\nPrevious conversation:\n{history_context}\n\nUser question: {question}\nAnswer:"

       
        llm = ChatGroq(model="openai/gpt-oss-120b", groq_api_key=GROQ_API_KEY)
        answer = llm.invoke(prompt)

        
        self.db.save_conversation(user_id, question, answer)

        return answer
   