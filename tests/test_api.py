import requests
from configuration import SERVICE_URL
from src.base_classes.response import Response
# from src.json_schema.post import MY_SCHEMA
from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200)
    response.validate(Post)
