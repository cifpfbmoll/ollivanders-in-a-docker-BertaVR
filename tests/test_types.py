from domain.types import *
import pytest


@pytest.mark.Backstage
def test_Backstage():
    assert Backstage("backstage_passes", 0, 15).update_quality() == 0
    assert Backstage("backstage_passes", 4, 15).update_quality() == 18
    assert Backstage("backstage_passes", 6, 15).update_quality() == 17
    assert Backstage("backstage_passes", 11, 0).update_quality() == 1
    assert Backstage("backstage_passes", 0, 50).update_quality() == 0


@pytest.mark.Conjured
def test_ConjuredItem():
    assert ConjuredItem("conjured_flask", 15, 20).update_quality() == 18
    assert ConjuredItem("conjured_flask", -3, 20).update_quality() == 16
    assert ConjuredItem("conjured_flask", -3, 0).update_quality() == 0


@pytest.mark.Normal
def test_NormalItem():
    assert NormalItem("Elixir of the Mongoose", 15, 20).update_quality() == 19
    assert NormalItem("Elixir of the Mongoose", -3, 20).update_quality() == 18
    assert NormalItem("Elixir of the Mongoose", -3, 0).update_quality() == 0


@pytest.mark.AgedBrie
def test_AgedBrie():
    assert AgedBrie("Aged Brie", 15, 20).update_quality() == 21
    assert AgedBrie("Aged Brie", -2, 20).update_quality() == 22
    assert AgedBrie("Aged Brie", 0, 20).update_quality() == 21
    assert AgedBrie("Aged Brie", 0, 50).update_quality() == 50
    assert AgedBrie("Aged Brie", 4, 50).update_quality() == 50
    assert AgedBrie("Aged Brie", -6, 50).update_quality() == 50
