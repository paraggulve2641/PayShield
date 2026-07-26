from fastapi import FastAPI

app = FastAPI(
    title="PayShield API",
    description="AI-Powered Banking Transaction Simulation & Fraud Detection Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PayShield API 🚀",
        "status": "Running Successfully"
    }