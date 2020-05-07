from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room_item = {
    'outside':   [Item("Coin","A bag of coins")],
    'foyer':     [Item("Pencil","numbes pencils for writing")],
    'overlook':  [Item("Figurine","A small figuring that can place on the table")], 
    'narrow':    [Item("Paper","a piece of paper to write on")],
    'treasure':  [Item("Mouse","A computer mouse to connect with computer")],
}
room['outside'].item = room_item['outside']
room['foyer'].item = room_item['foyer']
room['overlook'].item = room_item['overlook']
room['narrow'].item = room_item['narrow']
room['treasure'].item = room_item['treasure']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input('what is your name: ')
new_player = Player(user_name,room['outside'])


# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# 
while True:
    currentRoom =new_player.room
    print(f'Current Room:{currentRoom.name}, {currentRoom.description}.')
    for i in range (len(currentRoom.item)):
        print(f'Item: {currentRoom.item[i].name}, {currentRoom.item[i].description}')
    print(f'Take [item name] -> grab the item. or Drop [item name] -> put it down')
    action_input = input('What do you want to do? ')
    action_input1 = action_input.split(" ")
    if len(action_input1)==2:
        action = action_input1[0]
        item = action_input1[1]
        if action =='Take':
            print(type(currentRoom.item))
            if len(currentRoom.item)==0:
                print('There is no item in the room')
            else:
                for i in range(len(currentRoom.item)):
                    if item == currentRoom.item[i].name:
                        Item.on_take(currentRoom.item[i])
                        new_player.item.append(currentRoom.item[i])
                        currentRoom.item.pop(i)
                
                
                    else:
                        print('Invalid Input')
        elif action == 'Drop':
            for i in range(len(new_player.item)):
                print(new_player.item[i])
                if item == new_player.item[i].name:
                    Item.on_drop(new_player.item[i])
                    new_player.item.pop(i)
                else:
                    print("You don't have things to drop")
        else:
            print('Invalid Input')           
    else:
        print('Invalid Input')
            
       
       



    user_direction = input('Please enter one : [n] for North, [s] for South, [w] for West,[e] for East,[i] for inventory,[q] for quit: ')  
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    direction = ['n','s','w','e']
    if user_direction =='q':
       break
    elif user_direction in direction:
        new_player.changeRoom(user_direction)
    elif user_direction == 'i':
        if len(new_player.item) == 0:
            print("You don't have any inventory")
        else:
            print(new_player.inventory())
    else:
        print('Invalid Input')
   