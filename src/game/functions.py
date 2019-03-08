#player setup

#class player(health:100, backpack:[], size:5)
#class wolf(health:60, damage = 10, size:6)
#class bear(health:100, damage =15, size:6)
#lass monster(health:150, damage:33, size:8)

#inheritance

class living:
    def __init__(self, health, size):
        self.health = health
        self.size = size

class player(living):
    def __init__(self, health, size, backpack1, state1, locationX, locationY):
        living.__init__(self, health, size)
        self.backpack = backpack1
        self.state = state1
        self.locationX = locationX
        self.locationY = locationY
        #self.hunger = hunger1

    def useBandage(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        self.backpack["bandage"] -= 1

    #hunger doesnt change
    #need to decrease over time, or lose when hit
    def useFood(self):
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100
        self.backpack["food"] -= 1

    def check_death(self):
        if self.health <= 0:
            self.health = 0
            self.state = "dead"


class item:
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY


class bandage(item):
    def __init__(self,locationX, locationY):
        item.__init__(self, locationX, locationY)


class food(item):
    def __init__(self, locationX, locationY):
        item.__init__(self, locationX, locationY)


class bear(living):
    def __init__(self, health, size, damage):
        living.__init__(self, health, size)
        self.damage = damage


class wolf(living):
    def __init__(self, health, size, damage):
        living.__init__(self, health, size)
        self.damage = damage


class monster(living):
    def __init__(self, health, size, damage):
        living.__init__(self, health, size)
        self.damage = damage

#Example Backapcks
#dictionary backpack
#backpack = ["bandage":12, "food":20, "ammo":12, "shotgun":1 ,"pistol":1, "shotgun":1]

#large list of all items
#backpack1 = [bandage1, bandage2,food123, ammo123, shotgun1, ]

#pick up items and put it into backpack
def pickUpItem(currentPlayer, listOfItems):
    for currentItem in listOfItems:
        if currentPlayer.locationX == currentItem.locationX and currentPlayer.locationY == currentItem.locationY:
            #currentPlayer.backpack["bandage"]
            if isinstance(currentItem, bandage):
                currentPlayer.backpack["bandage"] += 1
            elif isinstance(currentItem, food):
                currentPlayer.backpack["food"] += 1
            #elif isinstance(currentItem, ammo):
                #currentPlayer.backpack["ammo"] += 1


#gun damage:    10/15/20   pistol/shotgun/rifle
#animal damage: 5/10/33    wolf/bear/monster
#used to know if a player was hit by a weapon/animal
#apply damage and update health
#def hitDetection(player, health):


#checks if a player has died
#if updated health is less than or equal to 0, kill player
def checkDeath(listOfPlayers):
    for currentPlayer in listOfPlayers:
        if currentPlayer.check_death() == "dead":
            listOfPlayers.remove(currentPlayer)

def addPlayers(newPlayer, listOfPlayers):
    listOfPlayers.append(newPlayer)

#def move(player):

#if a player reaches a world object or the edge, if move command is implemented, reject
#def restrictMove


#def main():
    #f __name__ == "__main__": main()