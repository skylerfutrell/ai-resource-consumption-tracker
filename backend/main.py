from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Calculation, engine, Base
from datetime import datetime

# This line makes sure the database file 'ai_usage.db' is created 
Base.metadata.create_all(bind=engine)

app = FastAPI()

# This is the "Key" to open the database for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "SQL Database Engine is Online"}

@app.get("/log-usage")
def log_usage(model: str, hours: float, location: str, db: Session = Depends(get_db)):
    # 1. Logic (The math)
    energy = 0.4 * hours
    water = energy * 1.2
    
    # 2. Create the SQL Object (The "Row")
    new_entry = Calculation(
        model_size=model,
        location=location,
        energy_kwh=energy,
        water_liters=water
    )
    
    # 3. Save to the Database
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    return {
        "status": "Success", 
        "database_id": new_entry.id, 
        "saved_data": {
            "model": model,
            "location": location,
            "carbon_g": energy * 300
        }
    }

@app.get("/view-database")
def view_database(db: Session = Depends(get_db)):
    # This is a SQL "SELECT *" command in Python
    all_history = db.query(Calculation).all()
    
    # We turn the SQL rows into a list we can read
    results = []
    for item in all_history:
        results.append({
            "id": item.id,
            "model": item.model_size,
            "location": item.location,
            "water": f"{item.water_liters}L",
            "time": item.timestamp.strftime("%Y-%m-%d %H:%M")
        })
    
    return {"total_records": len(results), "data": results}