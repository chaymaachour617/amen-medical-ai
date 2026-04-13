from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base

# Import des modèles pour que SQLAlchemy les enregistre
import app.models.patient
import app.models.exam
import app.models.session as session_model 
import app.models.alert
import app.models.message
import app.models.safety_log

# Import des routes
from app.api.routes import patient, exams, session, message, alerts, assistant

app = FastAPI(
    title="AMEN Medical AI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "AMEN backend running!"}

@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine) 
        connection = engine.connect()
        print("Database connected successfully!")
        connection.close()
    except Exception as e:
        print("Database connection failed:", e)

app.include_router(patient.router)
app.include_router(exams.router)
app.include_router(session.router)
app.include_router(message.router)
app.include_router(alerts.router)    
app.include_router(assistant.router)    
