import random
from room import Room

class Monster(Room):
    """
    Represents a room containing a monster
    """

    def __init__(self):
        """
        Initialize the monster with a random name and HP 
        """

        # call the parent Room constructor
        super().__init__()

        self._name = random.choice(["Orc", "Troll", "Goblin"])
        self._hp = random.randint(3, 10)

    def enter_room(self, player):
        """
        Have the player fight hte monster and receive rewards if defeated 
        """

        # check if the monster has already been defeated
        if self.character == ".":
            return "There is nothing here."
        
        # mark the room as containing a monster
        self._character = "M"

        result = f"There is a monster here!\n"
        result += f"{self._name} - HP: {self._hp}\n"

        # player attacks, has a 70 percent chance to hit the monster
        if random.randint(1, 10) <= 7:
            damage = random.randint(3, 6)
            self._hp -= damage
            result += f"You attack the {self._name} for {damage} damage.\n"
        else:
            result += "You try to attack, but miss!\n"
        
        # check whether the monster is still alive 
        if self._hp > 0:

            # monster has a 60 percent chance to hit the player 
            if random.randint(1, 10) <= 6:
                damage = random.randint(1, 5)
                player.take_dmg(damage)
                result += f"{self._name} attacks you for {damage} damage."
            else:
                result += f"{self._name} attacks, but misses!"
        
        else:
            # mark the room as empty after defeating the monster
            self._character = "."
            result += f"You have slain the {self._name}!\n"

            #give the player gold for defeating the monster
            gold = random.randint(1, 50)
            player.inc_gold(gold)
            result += f"You receive {gold} gold.\n"

            # 10 percent chance the monster was carrying a key
            if random.randint(1, 10) == 1:
                player.inc_key()
                result += "You found a key!"
        
        return result