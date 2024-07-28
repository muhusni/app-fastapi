from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "auth_v2"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    name = Column(String(255))
    NIP = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    
    employee = relationship("Employee", back_populates="user", uselist=False)