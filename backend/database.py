from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 1. This creates the database file on your computer
engine = create_engine("sqlite:///./ai_usage.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. This is the 'Blueprint' for our table
class Calculation(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    model_size = Column(String)
    location = Column(String)
    energy_kwh = Column(Float)
    water_liters = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)

# 3. Create the table for real
Base.metadata.create_all(bind=engine)