import pytest
import requests
from configuration import SERVICE_URL2, SERVICE_URL_TO_POST_DATA, user_test_data
from faker import Faker
from src.generator.player import Player

fake = Faker()

@pytest.fixture()
def get_player_generator():
    return Player()







# @pytest.fixture
# def user_fake_data():
#     return {
#         'name': fake.name(),
#         'job': fake.job()
#     }


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL2)
    return response


@pytest.fixture
def create_user(get_player_generator):
    print('START OF THE TEST')
    created_user = requests.post(url=SERVICE_URL_TO_POST_DATA, json=get_player_generator.build())
    print(get_player_generator.build())
    yield created_user
    print('END OF THE TEST')


