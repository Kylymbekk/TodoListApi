from utils.database import Base
from sqlalchemy import Column, Integer, DateTime, String, Boolean


class Example(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(String)
    dateEnd = Column(String)
    files = Column(String)
    isDone = Column(Boolean, default=False)
