import random
from room import Room

class Treasure(Room):
    """
    Represents a room containing treasure
    """
    def enter_room(self, player):
        """
        Give the player a key or gold if the room has not been visited 
        """

        #check if the treasure has already been collected
        if self.character == ".":
            return "There is nothing here."
        
        #mark the room as empty
        self._character = "."

        # 1 in 3 chances of finding the key
        if random.randint(1, 3) == 1:
            player.inc_key()
            return "You found a key!"
        
        else:
            gold = random.randint(1, 50)
            player.inc_gold(gold)
            return "You found some treasure!"
        

