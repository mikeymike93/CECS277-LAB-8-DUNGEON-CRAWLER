class Player:
    """
    Represents the player exploring the dungeon
    """

    def __init__(self):
        """
        Initialize the players starting stats
        """

        self._hp = 50
        self._gold = 0
        self._key = 0
        self._location = [0, 0]
        self._escaped = False
    
    @property
    def hp(self):
        """
        Return the players current hp
        """
        return self._hp
    
    @property
    def gold(self):
        """
        REturn the players current gold
        """
        return self._gold
    
    @property
    def key(self):
        """
        Return number of keys the player has 
        """
        return self._key
    
    @property
    def location(self):
        """
        Return the players current location
        """
        return self._location
    
    @property
    def escaped(self):
        """
        Return whether the player has escaped 
        """
        return self._escaped
    
    def take_dmg(self, dmg):
        """
        Subtract damage from the player's HP
        """

        self._hp -= dmg

        if self._hp < 0:
            self._hp = 0
    
    def inc_gold(self, g):
        """
        Increase the player's gold
        """

        self._gold += g

    def inc_key(self):
        """
        Add one key to the player
        """

        self._key += 1
    
    def escape(self):
        """
        Set the players escaped status to True
        """

        self._escaped = True
    
    def move(self, add_row, add_col):
        """ 
        Move the player to a new location
        """
        
        self._location[0] += add_row
        self._location[1] += add_col
    
    def __str__(self):
        """
        Return a string containing the players stats
        """
        return f"Player:\n HP = {self._hp}\n Gold = {self._gold}\n Keys = {self._key}"
        