import unittest
from repository.ActivityRepository import *
from domain.ActivityValidator import *
from controller.ActivityController import *
from repository.PersonRepository import *


def initLists():
    list1 = []
    a = Activity(101, [1010, 2020], date(2018, 3, 12), "14:00", "tennis")
    list1.append(a)
    a = Activity(404, [6060, 8080], date(2018, 5, 2), "14:00", "swimming")
    list1.append(a)
    a = Activity(110, [1111, 4040, 1110], date(2018, 8, 30), "14:00", "picnic")
    list1.append(a)
    list2 = []
    a = Activity(707, [8080, 2020], date(2018, 8, 12), "12:00", "family dinner")
    list2.append(a)
    a = Activity(808, [1110, 2020, 4040, 6060, 9090], date(2018, 8, 12), "10:00", "John's birthday")
    list2.append(a)
    a = Activity(909, [1010, 6060], date(2018, 8, 12), "16:00", "swimming")
    list2.append(a)
    a = Activity(110, [1111, 4040, 1110], date(2018, 8, 30), "14:00", "picnic")
    list2.append(a)
    list3 = []
    a = Activity(404, [6060, 8080], date(2018, 5, 2), "14:00", "swimming")
    list3.append(a)
    a = Activity(909, [1010, 6060], date(2018, 8, 12), "16:00", "swimming")
    list3.append(a)
    return list1, list2, list3

def initListDay():
    list = []
    a = Activity(808, [1110, 2020, 4040, 6060, 9090], date(2018, 8, 12), "10:00", "John's birthday")
    list.append(a)
    a = Activity(707, [8080, 2020], date(2018, 8, 12), "12:00", "family dinner")
    list.append(a)
    a = Activity(909, [1010, 6060], date(2018, 8, 12), "16:00", "swimming")
    list.append(a)
    return list


class ActivityControllerTest(unittest.TestCase):
    def setUp(self):
        actRepo = ActivityRepository()
        persRepo = PersonRepository()
        validator = ActivityValidator(actRepo, persRepo)
        self.controller = ActivityController(actRepo, validator)

    def testCreate(self):
        auxActivity = Activity(1, [1010, 2020, 7070], date(2018, 12, 6), "17:00", "chess")
        self.assertMultiLineEqual(str(self.controller.create(1, [1010, 2020, 7070], 2018, 12, 6, "17:00", "chess")), str(auxActivity))
        self.assertListEqual(self.controller.create(0, [1010, 1], 2016, 0, 0, "", ""), [" Void field(s)", " Invalid id! Id must be a positive integer", " Invalid time or date!"])

    def testDelete(self):
        self.assertEqual(self.controller.delete(101), None)
        self.assertEqual(self.controller.delete(101), "Activity not found!")

    def testFind(self):
        auxActivity = Activity(101, [1010, 2020], date(2018, 3, 12), "14:00", "tennis")
        self.assertMultiLineEqual(str(self.controller.find(101)), str(auxActivity))
        self.assertEqual(self.controller.find(1), None)

    def testUpdate(self):
        auxActivity = Activity(101, [1010, 2020], date(2018, 3, 12), "14:00", "tennis")
        auxActivity2 = Activity(101, [3030, 4040], date(2018, 4, 12), "17:00", "tennis")
        self.assertMultiLineEqual(str(self.controller.update(auxActivity, [3030, 4040], 2018, 4, 12, "17:00", "tennis")), str(auxActivity2))
        self.assertEqual(self.controller.update(auxActivity, [1, 2], 2017, 13, 12, "", ""), [" Void field(s)", " Id of participant not in the list!", " Invalid time or date!"])

    def testSearch(self):
        auxList1, auxList2, auxList3 = initLists()
        list1 = self.controller.search("14")
        list2 = self.controller.search("2018-08")
        list3 = self.controller.search("sw")
        poz = 0
        for act in list1:
            self.assertMultiLineEqual(str(act), str(auxList1[poz]))
            poz += 1
        poz = 0
        for act in list2:
            self.assertMultiLineEqual(str(act), str(auxList2[poz]))
            poz += 1
        poz = 0
        for act in list3:
            self.assertMultiLineEqual(str(act), str(auxList3[poz]))
            poz += 1

    def testGivenDay(self):
        auxList = initListDay()
        list = self.controller.givenDay(date(2018, 8, 12))
        poz = 0
        for act in list:
            self.assertMultiLineEqual(str(act), str(auxList[poz]))
            poz += 1

    def testList(self):
        auxRepo = ActivityRepository()
        self.assertMultiLineEqual(self.controller.list(), str(auxRepo))
