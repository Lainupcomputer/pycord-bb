from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, BigInteger, Text, JSON
from sqlalchemy.orm import relationship
from .base import Base
import datetime
from internal.timing import  current_time



class DataStorage(Base):
    __tablename__ = "data_storage"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(1024))
    data = Column(String(1024))

