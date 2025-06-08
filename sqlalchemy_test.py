from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    def __repr__(self):
        return f"<Employee(name={self.name}, age={self.age}, id={self.id})>"
engine = create_engine('sqlite:///employees.db', echo=True)

