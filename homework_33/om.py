from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create database engine
engine = create_engine('sqlite:///workspace.db')

# Base class for all models
Base = declarative_base()

# Define a sample table
class Workspace(Base):
    __tablename__ = 'workspace'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

# Create all tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

print("Database 'workspace' created successfully!")
print("Table 'workspace' created with columns: id, name, description, created_at")
