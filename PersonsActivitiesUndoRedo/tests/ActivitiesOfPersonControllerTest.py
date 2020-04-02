import unittest
from repository.ActivityRepository import *
from repository.PersonRepository import *
from controller.ActivitiesOfPersonController import *
from repository.ActivitiesOfPerson import *


def initListGA():
    list = []
    a = Activity(101, [1010, 2020], date(2018, 3, 12), "14:00", "tennis")
    list.append(a)
    a = Activity(606, [1010, 1111], date(2018, 5, 24), "16:00", "tennis")
    list.append(a)
    a = Activity(909, [1010, 6060], date(2018, 8, 12), "16:00", "swimming")
    list.append(a)
    return list

def initListUA():
    list = []
    p = Person(2020, "Mary", "0722222222", "Cluj, street 2, nr. 2")
    list.append(p)
    p = Person(4040, "Joana", "0744444444", "Cluj, street 4, nr. 4")
    list.append(p)
    p = Person(1010, "John", "0711111111", "Cluj, street 1, nr. 1")
    list.append(p)
    p = Person(6060, "Bron", "0766666666", "Cluj, street 6, nr. 6")
    list.append(p)
    p = Person(3030, "Mark", "0733333333", "Cluj, street 3, nr. 3")
    list.append(p)
    p = Person(8080, "Jimmy", "0788888888", "Cluj, street 8, nr. 8")
    list.append(p)
    p = Person(1110, "Marylin", "0712121212", "Cluj, street 10, nr. 10")
    list.append(p)
    p = Person(1111, "Cloe", "0713131313", "Cluj, street 11, nr. 11")
    list.append(p)
    p = Person(9090, "Jane", "0799999999", "Cluj, street 9, nr. 9")
    list.append(p)
    p = Person(5050, "Timmy", "0755555555", "Cluj, street 5, nr. 5")
    list.append(p)
    p = Person(7070, "Alex", "0777777777", "Cluj, street 7, nr. 7")
    list.append(p)
    listNumber = [5, 4, 3, 3, 2, 2, 2, 2, 1, 0, 0]
    return list, listNumber


class ActivitiesOfPersonControllerTest(unittest.TestCase):

    def setUp(self):
        persRepo = PersonRepository()
        actRepo = ActivityRepository()
        actPers = ActivitiesOfPerson(persRepo, actRepo)
        self.controller = ActivitiesOfPersonController(actPers)

    def testGetActivitiesOfAPerson(self):
        auxList = initListGA()
        list = self.controller.getActivitiesOfPerson(1010)
        poz = 0
        for day in list:
            self.assertMultiLineEqual(str(day), str(auxList[poz]))
            poz += 1
        list = self.controller.getActivitiesOfPerson(1)
        self.assertListEqual(list, [])

    def testUpcomingActivities(self):
        auxList, auxListNumber = initListUA()
        list, listNumber = self.controller.upcomingActivities()
        poz = 0
        for pers in list:
            self.assertMultiLineEqual(str(pers), str(auxList[poz]))
            poz += 1
        self.assertListEqual(auxListNumber, listNumber)

    def testDeleteId(self):
        self.controller.deleteId(1010)
        self.assertListEqual(self.controller.getActivitiesOfPerson(1010), [])
