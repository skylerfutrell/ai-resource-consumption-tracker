from fastapi import FastAPI

# This creates your app
app = FastAPI()

# This is the 'Home Page' of your backend
@app.get("/")
def home():
    return {"message": "AI Resource Tracker is Awake!"}

# This is the 'Calculator' part
@app.get("/calculate")
def estimate(hours: float = 1.0):
    # Simple math: 1 hour of AI = 0.5 liters of water used
    water = hours * 0.5
    return {"hours": hours, "water_used_liters": water}