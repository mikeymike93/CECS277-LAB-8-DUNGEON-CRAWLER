#Group 16
# Michael Sena
# Andrew Arroyos
# Lab Assignment 8 - This program creates a game called Dungeon Crawler, where the user moves around different rooms and looks
# for treasures while also trying to escape. User comes across monsters and needs to find a key before they can exit. If the user runs out of hitpoints when fighting the monsters they lose.

import random
from room import Room
from treasure import Treasure
from monster import Monster
from exit import Exit
from player import Player

def build_dungeon():
    """
    Build and return a random 5x5 dungeon

    Returns:
        list: 2D list containing the dungeon rooms
    """

    rooms = []

    #build the 5x5 dungeon

    #create 5 rows
    for row in range(5):
        new_row = []

        #create 5 cols for each row
        for col in range(5):
            
            roll = random.randint(1, 5)

            if roll == 1:
                room = Room()
            elif roll <= 3:
                room = Treasure()
            else:
                room = Monster()
            
            # add the room object to the current row
            new_row.append(room)
        
        # add the completed row to the dungeon
        rooms.append(new_row)

    #choose a random exit location
    exit_row = random.randrange(len(rooms))
    exit_col = random.randrange(len(rooms[0]))

    #so it doesnt get placed at the exit at the entrance
    while exit_row == 0 and exit_col == 0:
        exit_row = random.randrange(len(rooms))
        exit_col = random.randrange(len(rooms[0]))
    
    #place the selected room with an Exit object
    rooms[exit_row][exit_col] = Exit()

    # make the starting room an empty Room object
    rooms[0][0] = Room()

    return rooms

def display_dungeon(rooms, p):
    """
    Display the dungeon and player's position

    Args:
        rooms: the 2D list of room objects
        p: the player object
    """

    for row in range(len(rooms)):
        for col in range(len(rooms[row])):
            
            #check if the player is at this position
            if p.location == [row, col]:
                print("P", end=" ")
            else:
                #display the room's character
                print(rooms[row][col].character, end=" ")

        #move to the next line after each row
        print()

def main():
    """
    Runs the Dungeon game
    """

    #build the dungeon 
    rooms = build_dungeon()

    #create player
    p = Player()

    print("-Dungeon Crawler-")
    print("Find the key and find the exit to escape!")
    print("Treasure awaits, but watch out for monsters!")
    print("You enter the dungeon...")

    #enter the starting room 
    rooms[0][0].enter_room(p)

    # continue while the player is alive and has not escaped
    while p.hp > 0 and not p.escaped:

        #display players stats
        print(p)

        #display dungeon map
        display_dungeon(rooms, p)

        #ask player for a direction to go
        direction = input("Enter direction (wasd): ").lower().strip()

        # determine how the player will move 
        if direction == "w":
            add_row = -1
            add_col = 0
        elif direction == "s":
            add_row = 1
            add_col = 0
        elif direction == "a":
            add_row = 0
            add_col = -1
        elif direction == "d":
            add_row = 0
            add_col = 1
        else:
            print("Invalid direction.")
            continue

        #calculate the players possible new position
        new_row = p.location[0] + add_row
        new_col = p.location[1] + add_col

        #check that the new position is inside the dungeon 
        if (0 <= new_row < len(rooms) and 0 <= new_col < len(rooms[0])):

            #move the player
            p.move(add_row, add_col)

            #enter the room at the players new location
            print(rooms[p.location[0]][p.location[1]].enter_room(p))
        
        else:
            print("You cannot move outside the dungeon.")
    
    #display final dungeon 
    display_dungeon(rooms, p)

    #determine whether the player won or lost
    if p.escaped:
        print("You win!")
    
    else:
        print("You lose!")
    
    print("Game Over.")

main()