from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.organization import Organization
from app.models.user import User
from app.schemas.organization import OrganizationRegister
from app.auth.security import hash_password




def register_organization()