import shutil
import os
from fastapi import FastAPI, UploadFile, File, Form
from app.ingestion import process_pdf
from app.rag_engine import RAGEngine
from app.database import Base, engine, SessionLocal
from app.models import Conversation
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()
rag = RAGEngine()

@app.post("/upload")
async def upload_pdf(user_id: str = Form(...), file: UploadFile = File(...)):
    upload_path = f"storage/uploads/{user_id}.pdf"

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_pdf(upload_path, user_id)

    return {"message": "PDF processed successfully"}

@app.post("/ask")
def ask_question(user_id: str, question: str):
    try:
        answer = rag.ask(question, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    db = SessionLocal()
    conversation = Conversation(
        user_id=user_id,
        question=question,
        answer=answer
    )
    db.add(conversation)
    db.commit()
    db.close()

    return {"answer": answer}