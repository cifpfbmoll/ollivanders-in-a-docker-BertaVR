import pytest
from flask import Flask
from tests.configTest import client
from controller.items import Items


@pytest.mark.item
def test_item(client):
    rv = client.get("/items/Aged Brie")
    # assert b'{"name":"Aged Brie","sell_in": 3,"quality": 4}' in rv.data
    assert Items.get(Items, "Aged Brie") == rv.get_json()
