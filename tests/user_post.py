import requests
import unittest

from src.configuration import SERVICE_URL_TO_POST_DATA, user_test_data
from src.base_classes.response import Response
from src.pydantic_schemas.user import User, UserPost


def test_post_user_data():
    # Виклик POST-запиту для створення користувача
    resp = requests.post(url=SERVICE_URL_TO_POST_DATA, json=user_test_data)
    created_user = Response(resp)

    # Перевірка, що відповідь має код 201
    created_user.assert_status_code(201)

    # Валідація структури відповіді за допомогою класу UserPost
    created_user.validate(UserPost)

    # Перевірка, що дані користувача збігаються з вхідними даними
    created_user.assert_data(data='name', expected=user_test_data['name'])

    # Виведення JSON-відповіді для відладки
    print(resp.json())




# class TestUserData(unittest.TestCase):
#     def setUp(self):
#         # Відправлення POST-запиту для створення користувача та збереження відповіді
#         self.resp = requests.post(url=SERVICE_URL_TO_POST_DATA, json=user_test_data)
#         self.created_user = Response(self.resp)
#
#     def test_status_code(self):
#         # Перевірка, що відповідь на POST-запит має код 201
#         self.created_user.assert_status_code(201)
#
#     def test_data_validation(self):
#         # Валідація структури відповіді за допомогою класу UserPost
#         self.created_user.validate(UserPost)
#
#         # Перевірка, що дані користувача збігаються з вхідними даними
#         self.created_user.assert_data(data='name', expected=user_test_data['name'])
#
#     def test_get_user_data(self):
#         # Виклик GET-запиту для отримання створеного користувача
#         get_resp = requests.get(url=SERVICE_URL_TO_GET_DATA + f"/{self.created_user.id}")
#         get_user = Response(get_resp)
#
#         # Перевірка, що GET-запит повертає код 200
#         get_user.assert_status_code(200)
#
#         # Валідація структури відповіді за допомогою класу UserGet (припустимо, що такий клас існує)
#         get_user.validate(UserGet)
#
#
# if __name__ == '__main__':
#     unittest.main()


