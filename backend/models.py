from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    documents_sent = relationship("Document", back_populates="sender", foreign_keys="Document.sender_id")
    documents_received = relationship("Document", back_populates="receiver", foreign_keys="Document.receiver_id")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))

    sender = relationship("User", back_populates="documents_sent", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="documents_received", foreign_keys=[receiver_id])
