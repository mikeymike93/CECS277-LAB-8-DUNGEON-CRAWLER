from room import Room

class Exit(Room):
    """
    Represents the exit of the dungeon.
    """

    def enter_room(self, player):
        """
        Check if hte player has a key to escape the dungeon
        """
        self._character = "E"

        if player.key > 0:
            player.escape()
            return "You found the exit and escaped the dungeon!"
        else:
            return "You found the exit, but you need a key!"
        