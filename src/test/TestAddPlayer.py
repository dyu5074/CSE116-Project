import unittest

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


def addPlayers(newPlayer, listOfPlayers):
    listOfPlayers.append(newPlayer)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p1 = player(100, 5, {"bandage": 0, "food": 0}, "alive", 100, 100)
        p2 = player(100, 5, {"bandage": 1, "food": 2}, "alive", 14, 17)
        p3 = player(100, 5, {"bandage": 6, "food": 9}, "alive", 91, 3)
        p4 = player(100, 5, {"bandage": 5, "food": 2}, "alive", 34, 84)
        p5 = player(100, 5, {"bandage": 3, "food": 4}, "alive", 2, 372)
        p6 = player(100, 5, {"bandage": 7, "food": 8}, "alive", 352, 869)

        l1 = []

        addPlayers(p1, l1)
        addPlayers(p2, l1)
        addPlayers(p3, l1)
        addPlayers(p4, l1)
        addPlayers(p5, l1)

        self.assertEqual(p1 in l1, True)
        self.assertEqual(p2 in l1, True)
        self.assertEqual(p3 in l1, True)
        self.assertEqual(p4 in l1, True)
        self.assertEqual(p5 in l1, True)
        self.assertEqual(p6 in l1, False)


if __name__ == '__main__':
    unittest.main()
