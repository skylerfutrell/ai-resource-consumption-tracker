from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Calculation, engine, Base
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

# This line makes sure the database file 'ai_usage.db' is created 
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows all sites (including your React app) to talk to the API
    allow_credentials=True,
    allow_methods=["*"], # Allows GET, POST, etc.
    allow_headers=["*"], # Allows all custom headers
) 

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

@app.get("/stats/summary")
def get_summary_stats(db: Session = Depends(get_db)):
    # 1. Pull all records from your 'Calculation' table
    logs = db.query(Calculation).all()
    
    # 2. Sum up the actual columns in your database
    total_water = sum(log.water_liters for log in logs)
    total_energy = sum(log.energy_kwh for log in logs)
    total_carbon = total_energy * 300 # Using your 300g per kWh logic
    
    # 3. Return the dynamic data for the frontend
    return {
        "total_usage_events": len(logs),
        "metrics": {
            "water_liters": round(total_water, 2),
            "carbon_grams": round(total_carbon, 2),
            "energy_kwh": round(total_energy, 2)
        },
        "equivalents": {
            "smartphone_charges": round(total_carbon / 5, 1), 
            "plastic_bottles": round(total_water / 0.5, 1)
        }
    }