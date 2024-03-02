
from src.base_classes.response import Response
from src.pydantic_schemas.user import User


def test_get_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)




