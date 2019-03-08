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


def checkDeath(listOfPlayers):
    copy = []
    for currentPlayer in listOfPlayers:
        copy.append(currentPlayer)
    for currentPlayer in copy:
        if currentPlayer.state == "dead":
            listOfPlayers.remove(currentPlayer)
    #return listOfPlayers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p1 = player(100, 5, {"bandage": 10, "food": 12}, "alive", 123, 1234)
        p2 = player(100, 5, {"bandage": 10, "food": 12}, "dead", 123, 174)
        p3 = player(100, 5, {"bandage": 10, "food": 12}, "dead", 37, 134)
        p4 = player(100, 5, {"bandage": 10, "food": 12}, "alive", 17, 824)

        l1 = [p1, p2, p3, p4]

        checkDeath(l1)

        self.assertEqual(p1 in l1, True)
        self.assertEqual(p2 in l1, False)
        self.assertEqual(p3 in l1, False)
        self.assertEqual(p4 in l1, True)


if __name__ == '__main__':
    unittest.main()
