import email
from sqlalchemy import Boolean, Column, String, Enum, DateTime, Integer
from sqlalchemy.orm import relationships
import enum
from engine import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key = True)
    email = Column(String(50))
    hashedPassword = Column(String(255))
    secret = Column(String(25))
    phone = Column(String(15))
    admin = Column(Boolean())
    contractor = Column(Boolean())