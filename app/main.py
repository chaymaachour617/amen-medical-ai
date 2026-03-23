from fastapi import FastAPI
from app.db.session import engine

app = FastAPI(
    title="AMEN Medical AI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "AMEN backend running 🚀"}

@app.on_event("startup")
def test_connection():
    try:
        connection = engine.connect()
        print("✅ Database connected successfully!")
        connection.close()
    except Exception as e:
        print("❌ Database connection failed:", e)