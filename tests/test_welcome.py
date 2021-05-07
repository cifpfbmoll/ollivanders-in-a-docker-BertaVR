import pytest
from tests.configTest import client


@pytest.mark.welcome
def test_welcome(client):
    rv = client.get("/")
    assert b'{"Hello": "Ollivanders"}' in rv.data
