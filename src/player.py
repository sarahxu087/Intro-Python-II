# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self,name,room,item=[]):
        self.name = name
        self.room = room
        self.item = item

    def inventory(self):
        for i in range (len(self.item)):
            print(f'Inventory: {self.item[i].name}')
    
    def changeRoom(self,direction):
        if direction =='n':
            if self.room.n_to != None:
                self.room = self.room.n_to
            else:
                print('wrong dirction')
        elif direction == 's':
            if self.room.s_to != None:
                self.room = self.room.s_to
            else:
                print('wrong dirction')
        elif direction == 'w':
            if self.room.w_to != None:
                self.room = self.room.w_to
            else:
                print('wrong dirction')
        elif direction == 'e':
            if self.room.e_to != None:
                self.room = self.room.e_to
            else:
                print('wrong dirction')
        else:
            print('wrong dirction')
