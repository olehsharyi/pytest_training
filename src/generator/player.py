
from faker import Faker
from random import randint

fake = Faker()


class Player:
    """

    Class to generate random test data:
    included such field as:

    - Name
    - Age

    """

    def __init__(self):
        self.result = {}
        self.default()

    def set_name(self, name=fake.name()):

        self.result["name"] = name

        return self

    def set_age(self, age=randint(18, 90)):

        self.result["age"] = age

        return self

    def build(self):
        return self.result

    def default(self):
        self.set_age()
        self.set_name()
        self.result['country'] = {
            "US": fake.city(),
            "non-US": fake.city()
        }
        return self


x = Player()
print(x.build())
