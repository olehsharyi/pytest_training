import requests
from src.configuration import SERVICE_URL2
from src.base_classes.response import Response
from src.pydantic_schemas.user import User


def test_get_users_list():
    resp = requests.get(SERVICE_URL2)
    response = Response(resp)
    response.assert_status_code(200)
    response.validate(User)
