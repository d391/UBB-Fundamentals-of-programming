import unittest
from controller.PersonController import *
from domain.PersonValidator import *
from repository.PersonRepository import *


def initLists():
    list1 = []
    p = Person(1010, "John", "0711111111", "Cluj, street 1, nr. 1")
    list1.append(p)
    p = Person(1110, "Marylin", "0712121212", "Cluj, street 10, nr. 10")
    list1.append(p)
    p = Person(1111, "Cloe", "0713131313", "Cluj, street 11, nr. 11")
    list1.append(p)
    list2 = []
    p = Person(2020, "Mary", "0722222222", "Cluj, street 2, nr. 2")
    list2.append(p)
    p = Person(3030, "Mark", "0733333333", "Cluj, street 3, nr. 3")
    list2.append(p)
    p = Person(1110, "Marylin", "0712121212", "Cluj, street 10, nr. 10")
    list2.append(p)
    return list1, list2


class PersonControllerTest(unittest.TestCase):
    def setUp(self):
        repo = PersonRepository()
        validator = PersonValidator(repo)
        self.controller = PersonController(repo, validator)

    def testCreate(self):
        auxPerson = Person(1, "Luca", "0745202147", "Oradea, street 12, nr. 12")
        self.assertMultiLineEqual(str(self.controller.create(1, "Luca", "0745202147", "Oradea, street 12, nr. 12")), str(auxPerson))
        self.assertListEqual(self.controller.create(0, "luca", "0745", "Oradea, street 12, nr. 12"), [" Invalid id! Please introduce a positive integer!", " Name must start with a capital letter!", " Invalid phone number!"])

    def testDelete(self):
        self.assertEqual(self.controller.delete(2020), None)
        self.assertEqual(self.controller.delete(2020), "Person not found!")

    def testFind(self):
        auxPerson = Person(2020, "Mary", "0722222222", "Cluj, street 2, nr. 2")
        self.assertMultiLineEqual(str(self.controller.find(2020)), str(auxPerson))
        self.assertEqual(self.controller.find(1), None)

    def testUpdate(self):
        auxPerson = Person(2020, "Mary", "0722222222", "Cluj, street 2, nr. 2")
        auxPerson2 = Person(2020, "Luca", "0745202147", "Oradea, street 12, nr. 12")
        self.assertMultiLineEqual(str(self.controller.update(auxPerson, "Luca", "0745202147", "Oradea, street 12, nr. 12")), str(auxPerson2))
        self.assertListEqual(self.controller.update(auxPerson, "mary", "0745", ""), [" Empty fields!", " Name must start with a capital letter!", " Invalid phone number!"])

    def testSearch(self):
        auxList1, auxList2 = initLists()
        list1 = self.controller.search("071")
        list2 = self.controller.search("Mar")
        poz = 0
        for pers in list1:
            self.assertMultiLineEqual(str(pers), str(auxList1[poz]))
            poz += 1
        poz = 0
        for pers in list2:
            self.assertMultiLineEqual(str(pers), str(auxList2[poz]))
            poz += 1
        #self.assertListEqual(self.controller.search("Mar"), list2) ??
        self.assertEqual(self.controller.search("hhh"), [])

    def testList(self):
        auxRepo = PersonRepository()
        self.assertTrue(self.controller.list(), str(auxRepo))
