from datetime import datetime
import email
from email.policy import default
from multiprocessing.pool import CLOSE
from tkinter.font import NORMAL
from psycopg2 import Date
from sqlalchemy import Boolean, Column, String, Enum, DateTime, Integer, Table, ForeignKey
from sqlalchemy.orm import relationships, relationship
import enum
from engine import Base
from datetime import datetime, timezone

# приоритет: Обычная, Высокий, Критический;
class Priority(Enum):
    NORMAL = 0
    HIGH = 1
    CRITICAL = 2

# Статус – в работе, в ожидании, закрыта предварительно, закрыта;
class Status(Enum):
    IN_WORK = 0
    IN_WAIT = 1
    PRE_CLOSED = 2
    CLOSED = 3

class Role(Enum):
    DEALER = 0
    CONTRACTOR = 1
    ADMIN = 2

users_applications = Table(
    "association",
    Base.metadata,
    Column("users_id", ForeignKey("users.id")),
    Column("applications_id", ForeignKey("applications.id")),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(50))
    phone = Column(String(15))
    hashedPassword = Column(String(255))
    secret = Column(String(25))

    applications = relationships("Application", secondary=users_applications, back_populates="users")
    

    # N to N
    # applications = 


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key = True)
    theme = Column(String)
    title = Column(String)
    text = Column(String)
    
    # user = Column(Enum(Role), default=Role.DEALER)

    # contactor_admin = Column(Enum(Role), default=Role.CONTRACTOR)
    
    users = relationship(
        "Parent", secondary=association_table, back_populates="children"
    )

    priority = Column(Enum(Priority), default=Priority.NORMAL)
    status = Column(Enum(Status), default=Status.IN_WORK)

    date_submission = Column(DateTime, default=datetime.now(timezone.utc))
    date_closing = Column(DateTime, default=None)

    


