from zdd_rooms import UndergroundLake
from main_classes import Item


def test_initial_state():
    """Test the initial state of the UndergroundLake."""
    lantern = Item("Mysterious Lantern", "A lantern emitting a calming light.", movable=True)
    lake_room = UndergroundLake(
        name="The Underground Lake",
        description="A vast, dark room with a silent lake and a mysterious lantern on a platform.",
        items=[lantern]
    )
    assert lake_room.monsters_awake is False
    assert lake_room.treasure_found is False
    assert len(lake_room.items) == 1

def test_treasure_logic():
    """Test if the treasure can be found with the lantern."""
    lantern = Item("Mysterious Lantern", "A lantern emitting a calming light.", movable=True)
    lake_room = UndergroundLake(
        name="The Underground Lake",
        description="A vast, dark room with a silent lake and a mysterious lantern on a platform.",
        items=[lantern]
    )
    user_inventory = [lantern]
    lake_room.treasure_found = False

    if not lake_room.treasure_found:
        treasure = Item("Golden Necklace", "A shiny necklace made of pure gold.", movable=True)
        user_inventory.append(treasure)
        lake_room.treasure_found = True

    assert any(item.name == "Golden Necklace" for item in user_inventory)
    assert lake_room.treasure_found is True
