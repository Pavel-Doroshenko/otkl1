import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Resource_shutdowns(Base):
    __tablename__ = 'resource shutdowns'

    id = Column(Integer,primary_key=True)
    recording_date = Column(String(250), nullable=False)
    adress = Column(String(250), nullable=False)
    type_of_resource = Column(String(250), nullable=False)
    shutdown_date = Column(String(250), nullable=False)
    renewal_date = Column(String(250), nullable=False)

engine = create_engine('sqlite:///shutdowns.db')
Base.metadata.create_all(engine)