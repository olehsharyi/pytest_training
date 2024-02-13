from pydantic import BaseModel, field_validator,Field


class Post(BaseModel):
    id: int = Field(..., ge=200)
    brand: str

    # @field_validator("id")
    # def check_len_id(cls, v):
    #     if v < 3:
    #         raise ValueError("len ID is not expected")
    #     else:
    #         return v

    # [{'id': 2686, 'uid': '408edd93-3c44-4e19-8b96-561423fecf65', 'brand': 'Leffe',