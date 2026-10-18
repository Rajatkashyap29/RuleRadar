from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.database import Base,engine
from app.models.organization import Organization
from app.models.user import User

app = FastAPI(
    title="RuleRadar API",
    description="AI-powered business rule conflict detection platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["Health"])
def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "RuleRadar API is running"
        }
    )