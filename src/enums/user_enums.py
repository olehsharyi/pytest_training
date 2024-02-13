from enum import Enum

class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    inactive = 'inactive'
    active = 'active'


class UserErrors(Enum):
    not_valid_email = 'Email is not valid'