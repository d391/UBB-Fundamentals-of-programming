import random


class PersonGenerator:

    def generateId(self):
        return random.choice(range(1000, 10000))

    def generateName(self):
        names = ["Oliver", "Jake", "Noah", "James", "Jack", "Connor", "Liam", "John", "Harry", "Callum", "Mason", "Robert",
                 "Amelia", "Margaret", "Emma", "Mary", "Olivia", "Samantha", "Olivia", "Patricia", "Isla", "Bethany",
                 "Sophia", "Jennifer", "Emily", "Elizabeth", "Isabella"]
        return random.choice(names)

    def generatePhoneNumber(self):
        phoneNumber = "07"
        for i in range(8):
            phoneNumber += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        return phoneNumber

    def generateAddress(self):
        cities = ["Cluj", "Oradea", "Bucuresti", "Constanta", "Brasov", "Arad", "Sibiu", "Alba Iulia", "Deva", "Brad", "Iasi"]
        streets = ["Iunie", "Zorilor", "Dorobanti", "Dacia", "Eroilor", "Libertatii", "Observatorului", "Ion Popa"]
        return random.choice(cities) + ", street: " + random.choice(streets) + ", nr: " + str(random.choice(range(1, 151)))
