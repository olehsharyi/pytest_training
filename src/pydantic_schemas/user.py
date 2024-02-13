from pydantic import BaseModel, field_validator, Field
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator('email')
    def check_email_address(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(UserErrors.not_valid_email.value)
