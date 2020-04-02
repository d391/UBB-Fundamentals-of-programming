from repository.PersonRepository import *
from domain.PersonGenerator import *
from domain.ActivityGenerator import *


def initListGen(persRepo):
    idList = []
    nr = 0
    while nr < 100:
        g = PersonGenerator()
        p = Person(g.generateId(), g.generateName(), g.generatePhoneNumber(), g.generateAddress())
        if p.id not in idList:
            nr += 1
            persRepo.store(p)
            idList.append(p.id)


def initListPers(persRepo):
    p = Person(1010, "John", "0711111111", "Cluj, street 1, nr. 1")
    persRepo.store(p)
    p = Person(2020, "Mary", "0722222222", "Cluj, street 2, nr. 2")
    persRepo.store(p)
    p = Person(3030, "Mark", "0733333333", "Cluj, street 3, nr. 3")
    persRepo.store(p)
    p = Person(4040, "Joana", "0744444444", "Cluj, street 4, nr. 4")
    persRepo.store(p)
    p = Person(5050, "Timmy", "0755555555", "Cluj, street 5, nr. 5")
    persRepo.store(p)
    p = Person(6060, "Bron", "0766666666", "Cluj, street 6, nr. 6")
    persRepo.store(p)
    p = Person(7070, "Alex", "0777777777", "Cluj, street 7, nr. 7")
    persRepo.store(p)
    p = Person(8080, "Jimmy", "0788888888", "Cluj, street 8, nr. 8")
    persRepo.store(p)
    p = Person(9090, "Jane", "0799999999", "Cluj, street 9, nr. 9")
    persRepo.store(p)
    p = Person(1110, "Marylin", "0712121212", "Cluj, street 10, nr. 10")
    persRepo.store(p)
    p = Person(1111, "Cloe", "0713131313", "Cluj, street 11, nr. 11")
    persRepo.store(p)


def getAllParticipants(persRepo):
    list = []
    for pers in persRepo.getAllPersons():
        list.append(pers.id)
    return list


def initListGenAct(persRepo, actRepo):
    listDate = []
    idList = []
    nr = 0
    participants = getAllParticipants(persRepo)
    while nr < 100:
        g = ActivityGenerator()
        a = Activity(g.generateId(), g.generatePersIds(participants), g.generateDate(), g.generateTime(), g.generateDescription())
        if a.date not in listDate and a.activityId not in idList:
            nr += 1
            listDate.append(a.date)
            idList.append(a.activityId)
            actRepo.store(a)


def initListActs(actRepo):
    a = Activity(101, [1010, 2020], date(2018, 3, 12), "14:00", "tennis")
    actRepo.store(a)
    a = Activity(202, [2020, 3030], date(2018, 3, 17), "16:00", "tennis")
    actRepo.store(a)
    a = Activity(303, [3030, 4040], date(2018, 4, 30), "16:00", "picnic")
    actRepo.store(a)
    a = Activity(404, [6060, 8080], date(2018, 5, 2), "14:00", "swimming")
    actRepo.store(a)
    a = Activity(505, [4040, 2020], date(2018, 5, 15), "16:00", "football")
    actRepo.store(a)
    a = Activity(606, [1010, 1111], date(2018, 5, 24), "16:00", "tennis")
    actRepo.store(a)
    a = Activity(707, [8080, 2020], date(2018, 8, 12), "12:00", "family dinner")
    actRepo.store(a)
    a = Activity(808, [1110, 2020, 4040, 6060, 9090], date(2018, 8, 12), "10:00", "John's birthday")
    actRepo.store(a)
    a = Activity(909, [1010, 6060], date(2018, 8, 12), "16:00", "swimming")
    actRepo.store(a)
    a = Activity(110, [1111, 4040, 1110], date(2018, 8, 30), "14:00", "picnic")
    actRepo.store(a)
