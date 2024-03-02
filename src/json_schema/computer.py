from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from src.enums.user_enums import Statuses
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Network, IPv6Network
from pydantic.color import Color

from tests.examples import computer


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Network
    host_v6: IPv6Network
    detailed_info: DetailedInfo


comp = Computer.model_validate(computer)

print(comp)
