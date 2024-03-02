from enum import Enum

class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    inactive = 'INACTIVE'
    active = 'ACTIVE'


class UserErrors(Enum):
    not_valid_email = 'Email is not valid'