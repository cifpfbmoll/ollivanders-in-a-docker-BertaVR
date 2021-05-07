import pytest
from flask import Flask
from tests.configTest import client
from controller.objeto import Objeto


@pytest.mark.objeto
def test_objeto(client):
    rv = client.get("/objeto/Aged Brie")
    # assert b'{"name":"Aged Brie","sell_in": 3,"quality": 4}' in rv.data
    assert {"name": "Aged Brie", "quality": 4, "sell_in": 3} == rv.get_json()
