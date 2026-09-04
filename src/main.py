from fastapi import FastAPI

app = FastAPI(title="CropGuard Demo")


@app.get("/")
def home():
    return {
        "project": "CropGuard",
        "message": "SIH 2026 demo repository is working",
    }
