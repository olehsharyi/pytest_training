from src.base_classes.response import Response
from src.pydantic_schemas.user import UserPost
import pytest


def test_post_user_data(create_user, get_player_generator):
    Response(create_user).assert_status_code(201)
    Response(create_user).validate(UserPost)
    Response(create_user).assert_data(data='name', expected=get_player_generator.build()['name'])



