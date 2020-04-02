import unittest
from controller.DayController import *
from repository.DayRepository import *
from repository.ActivityRepository import *


def initList():
    list = []
    d = Day(date(2018, 8, 12), 3)
    list.append(d)
    d = Day(date(2018, 8, 30), 1)
    list.append(d)
    d = Day(date(2018, 5, 24), 1)
    list.append(d)
    d = Day(date(2018, 5, 15), 1)
    list.append(d)
    d = Day(date(2018, 5, 2), 1)
    list.append(d)
    d = Day(date(2018, 4, 30), 1)
    list.append(d)
    d = Day(date(2018, 3, 17), 1)
    list.append(d)
    d = Day(date(2018, 3, 12), 1)
    list.append(d)
    return list


class DayControllerTest(unittest.TestCase):

    def setUp(self):
        repo = DaysRepository()
        actRepo = ActivityRepository()
        self.controller = DayController(repo, actRepo)

    def testDays(self):
        auxList = initList()
        list = self.controller.storeDays()
        poz = 0
        for day in list:
            self.assertMultiLineEqual(str(day), str(auxList[poz]))
            poz += 1



"""
Day: 30 of August 2018
 Number of activities: 1

Day: 24 of May 2018
 Number of activities: 1

Day: 15 of May 2018
 Number of activities: 1

Day: 2 of May 2018
 Number of activities: 1

Day: 30 of April 2018
 Number of activities: 1

Day: 17 of March 2018
 Number of activities: 1

Day: 12 of March 2018
 Number of activities: 1
"""