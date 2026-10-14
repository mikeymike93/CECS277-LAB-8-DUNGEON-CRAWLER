class Room:
    """
    Represents an empty room.
    """

    def __init__(self):
        """
        Initializes the rooms character to a dash
        """
        self._character = "-"
    
    @property
    def character(self):
        """
        Returns the rooms character
        """
        return self._character
    
    def enter_room(self, player):
        """
        Mark the room as visited adn return a message
        """
        self._character = "."
        return "There is nothing here."