import unittest


class living:
    def __init__(self, health, size):
        self.health = health
        self.size = size


class player(living):
    def __init__(self, health, size, backpack1, state1, locationX, locationY):
        living.__init__(self,health, size)
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
    def __init__(self, locationX, locationY,):
        item.__init__(self, locationX, locationY)


def pickUpItem(currentPlayer, listOfItems):
    for currentItem in listOfItems:
        if currentPlayer.locationX == currentItem.locationX and currentPlayer.locationY == currentItem.locationY:
            #currentPlayer.backpack["bandage"]
            if isinstance(currentItem, bandage):
                currentPlayer.backpack["bandage"] += 1
            elif isinstance(currentItem, food):
                currentPlayer.backpack["food"] += 1
class MyTestCase(unittest.TestCase):

    def test_function_pickUpItem(self):
        p1 = player(100, 5, {"bandage": 0, "food": 0}, "alive", 100, 100)
        p2 = player(100, 5, {"bandage": 1, "food": 2}, "alive", 14, 17)
        p3 = player(100, 5, {"bandage": 6, "food": 9}, "alive", 91, 3)
        p4 = player(100, 5, {"bandage": 5, "food": 2}, "alive", 34, 84)
        p5 = player(100, 5, {"bandage": 3, "food": 4}, "alive", 2, 372)
        p6 = player(100, 5, {"bandage": 7, "food": 8}, "alive", 352, 869)

        i1 = bandage(100, 100)
        i2 = bandage(234, 567)
        i3 = bandage(0, 0)
        i4 = food(2, 372)
        i5 = food(1000, 1000)
        i6 = food(134, 987)

        l1 = [i1, i3, i5]
        l2 = [i2, i4, i6]
        l3 = [i1, i2, i3]
        l4 = [i4, i5, i6]

        pickUpItem(p1, l1)
        pickUpItem(p2, l2)
        pickUpItem(p3, l3)
        pickUpItem(p4, l4)
        pickUpItem(p5, l4)
        pickUpItem(p6, l3)

        self.assertEqual(p1.backpack["bandage"], 1)
        self.assertEqual(p2.backpack["bandage"], 1)
        self.assertEqual(p3.backpack["bandage"], 6)
        self.assertEqual(p4.backpack["food"], 2)
        self.assertEqual(p5.backpack["food"], 5)
        self.assertEqual(p6.backpack["food"], 8)


if __name__ == '__main__':
    unittest.main()
