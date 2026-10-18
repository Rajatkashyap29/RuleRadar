from pydantic import BaseModel, EmailStr, Field


class OrganizationRegister(BaseModel):
    organization_name: str = Field(min_length=2, max_length=150)
    admin_name: str = Field(min_length=2, max_length=100)
    admin_email: EmailStr
    password: str = Field(min_length=8)