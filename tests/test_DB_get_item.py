import pytest
from repository.db import DB


@pytest.mark.db
def test_get_item():
    item = ["Aged Brie", 3, 4]
    assert [item] == DB.get_item("Aged Brie")
