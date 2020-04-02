import random
from datetime import date
from domain.ActivityValidator import *
from domain.Activity import *


class ActivityGenerator:
    def generateId(self):
        return random.choice(range(100, 1000))

    def generatePersIds(self, listIds):
        persIds = []
        number = random.choice(range(1, 15))
        for i in range(number):
            id = random.choice(listIds)
            if id not in persIds:
                persIds.append(id)
            else:
                i -= 1
        return persIds

    def generateDate(self):
        year = random.choice([2017, 2018])
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 28))
        return date(year, month, day)

    def generateTime(self):
        digit1 = random.choice(range(0, 3))
        digit2 = random.choice(range(0, 4))
        digit3 = random.choice(range(0, 6))
        digit4 = random.choice(range(0, 10))
        return str(digit1) + str(digit2) + ":" + str(digit3) + str(digit4)

    def generateDescription(self):
        descriprions = ["Baseball", "Basketball", "Beekeeping", "Bird watching", "Blacksmithing", "BMX", "Board sports", "Bodybuilding", "Brazilian jiu-jitsu", "Camping", "Canoeing", "Canyoning", "Dowsing", "Driving", "Fishing", "Flag football", "Flying", "Flying disc", "Foraging", "Freestyle football", "Gardening", "Geocaching", "Ghost hunting", "Graffiti", "Handball"]
        return random.choice(descriprions).lower()
