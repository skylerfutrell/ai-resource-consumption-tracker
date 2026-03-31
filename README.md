# AI Resource Consumption Tracker

## Overview
This project estimates and visualizes the energy and water consumption of artificial intelligence systems. It models AI usage, stores results in a database, and presents insights through an interactive dashboard.

## Goals
- Model AI energy and water usage
- Build a data pipeline using Python and SQL
- Develop a backend API with FastAPI
- Create a frontend dashboard for visualization
- Explore ethical implications of AI resource consumption

## Tech Stack
- Backend: Python, FastAPI, SQLAlchemy
- Database: SQLite (SQLAlchemy ORM)
- Frontend: React (Vite), Tailwind CSS
- Data Science: Pandas (for future analysis)

## Project Structure
- **/backend**: FastAPI server, SQLAlchemy database models, and AI consumption logic.
- **/frontend**: React dashboard styled with Tailwind CSS, fetching live data via API.
- **ai_usage.db**: Local SQLite database storing all resource calculation history.

## Getting Started
1. **Backend**: `cd backend` -> `pip install -r requirements.txt` -> `uvicorn main:app --reload`
2. **Frontend**: `cd frontend` -> `npm install` -> `npm run dev`
