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

class SenderInfo(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class ReceiverInfo(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class DocumentResponse(BaseModel):
    id: int
    title: str
    sender: SenderInfo
    receiver: ReceiverInfo  # Добавляем получателя

    class Config:
        orm_mode = True
        from_attributes = True

from typing import Literal



@router.get("/documents", response_model=list[DocumentResponse])
def get_documents(
    type: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if type == "incoming":
        documents = (
            db.query(Document)
            .filter(Document.receiver_id == current_user.id)
            .join(User, Document.sender_id == User.id)
            .add_columns(User.id.label("sender_id"), User.username.label("sender_username"))
            .all()
        )
        return [
            {
                "id": doc.id,
                "title": doc.title,
                "sender": {"id": sender_id, "username": sender_username},
                "receiver": {"id": current_user.id, "username": current_user.username},  # Добавляем receiver
            }
            for doc, sender_id, sender_username in documents
        ]
    elif type == "outgoing":
        documents = (
            db.query(Document)
            .filter(Document.sender_id == current_user.id)
            .join(User, Document.receiver_id == User.id)
            .add_columns(User.id.label("receiver_id"), User.username.label("receiver_username"))
            .all()
        )
        return [
            {
                "id": doc.id,
                "title": doc.title,
                "sender": {"id": current_user.id, "username": current_user.username},
                "receiver": {"id": receiver_id, "username": receiver_username},
            }
            for doc, receiver_id, receiver_username in documents
        ]
    else:
        raise HTTPException(status_code=400, detail="Invalid document type")






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
