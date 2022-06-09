from sqlalchemy import Column,String,Integer
from base import Base

class ToDo(Base):
    __tablename__ = "ToDo"

    id = Column(Integer,primary_key=True)
    title = Column(String(25))
    description = Column(String(75))

    def __init__(self,title,description):
        self.title = title
        self.description = description

    def setTitle(self,title):
        self.title = title
    def setDescription(self,description):
        self.description = description

    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description