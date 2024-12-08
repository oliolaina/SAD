from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User, Document
from pydantic import BaseModel
from routers.auth import get_current_user

router = APIRouter()

class DocumentCreate(BaseModel):
    receiver: str
    title: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    sender_id: int
    receiver_id: int

    class Config:
        from_attributes = True

from typing import Literal

@router.get("/documents", response_model=list[DocumentResponse])
def get_documents(
    type: Literal["incoming", "outgoing"],  # Ограничиваем допустимые значения
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    print("get_documents")
    if type == "incoming":
        documents = db.query(Document).filter(Document.receiver_id == current_user.id).all()
    elif type == "outgoing":
        documents = db.query(Document).filter(Document.sender_id == current_user.id).all()
    else:
        raise HTTPException(status_code=400, detail="Invalid document type")

    print("Возвращаемые документы:", documents)
    return documents




@router.post("/documents", response_model=DocumentResponse)
def create_document(
    doc: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    receiver = db.query(User).filter(User.username == doc.receiver).first()
    if not receiver:
        raise HTTPException(status_code=400, detail="Receiver not found")
    new_doc = Document(
        title=doc.title,
        sender_id=current_user.id,
        receiver_id=receiver.id
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc
