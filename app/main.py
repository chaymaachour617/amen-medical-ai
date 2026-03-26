from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.db.session import engine
import app.models.patient
import app.models.exam
import app.models.session
import app.models.message
import app.models.alert
import app.models.safety_log
from app.api.routes import patient, exam, session, message

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
        print(" Database connected successfully!")
        connection.close()
    except Exception as e:
        print(" Database connection failed:", e)

app.include_router(patient.router)
app.include_router(exam.router)
app.include_router(session.router)
app.include_router(message.router)



Base.metadata.create_all(bind=engine)       