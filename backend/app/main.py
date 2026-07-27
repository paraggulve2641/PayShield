from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="PayShield API",
    description="AI Powered Banking Transaction Simulation Platform",
    version="1.0.0"
)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to PayShield API 🚀",
        "status": "Server Running"
    }

# Health Check API
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "server": "Running",
        "database": "Not Connected Yet"
    }

# About API
@app.get("/about")
def about():
    return {
        "project": "PayShield",
        "developer": "Parag Gulve",
        "version": "1.0",
        "purpose": "Banking Transaction Simulation Platform"
    }