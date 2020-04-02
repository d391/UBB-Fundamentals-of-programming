from domain.Person import *
from domain.Iterable import Iterable
import pickle
import copy


class PersonRepository:
    def __init__(self):
        self._persRepo = Iterable()

    def store(self, person):
        """
        Stores a person in the repository
        Input:
            - person: Person
        Output:
            - updated version of repository
        """
        self._persRepo.append(person)

    def find(self, persId):
        """
        Searches for and returns an person using its id
            Input:
                - persId: integer
            Output:
                - person: Person (if it is found)
                - None, otherwise
        """
        for pers in self._persRepo:
            if persId == pers.id:
                return pers
        return None

    def update(self, person, newPerson):
        """
        Updates the data of a given person
        Input:
            - person: Person
            - newName: string
            - newPhoneNr: string
            - newAddress: string
        Output:
            - updated version of person
        """
        index = 0
        for pers in self._persRepo:
            if pers.id == person.id:
                self._persRepo.__setitem__(index, newPerson)
                return newPerson
            index += 1

    def delete(self, pers):
        self._persRepo.remove(pers)

    def getAllPersons(self):
        """
        Return all the elements of the repository
        Input: -
        Output:
            - persRepo: repository
        """
        return self._persRepo

    def search(self, choice):
        """
        Returns all the persons that have the given criteria
        Input:
            - choice: string
        Output:
            - results: list
        """
        results = []
        for pers in self._persRepo:
            if choice in pers.name[0:] or choice in pers.phoneNumber[0:]:
                results.append(pers)
        return results

    def __str__(self):
        """
        String format of the person repository
        Input: -
        Output:
            - text: string
        """
        text = ""
        for pers in self._persRepo:
            text += str(pers)
            text += "\n"
        return text

    def __len__(self):
        return len(self._persRepo)


class PersonTextFileRepo(PersonRepository):

    def __init__(self, fileName = "persons.txt"):
        PersonRepository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def store(self, pers):
        PersonRepository.store(self, pers)
        self._saveFile()

    def delete(self, pers):
        PersonRepository.delete(self, pers)
        self._saveFile()

    def update(self, person, newPerson):
        PersonRepository.update(self, person, newPerson)
        self._saveFile()

    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for pers in self.getAllPersons():
                f.write(str(pers.id) + "          " + pers.name + "          " + pers.phoneNumber + "          " + pers.address + "\n")
        except IOError as e:
            print("Cannot load file" + str(e))
        finally:
            f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline()
            while len(line) > 2:
                tok = line.split("          ")
                pers = Person(int(tok[0].strip()), tok[1], tok[2], tok[3].strip())
                PersonRepository.store(self, pers)
                line = f.readline()
        except IOError as e:
            print("Cannot load file" + str(e))
        finally:
            f.close()


class PersonBinaryRepo(PersonRepository):

    def __init__(self, fileName = "persons.pickle"):
        PersonRepository.__init__(self)
        self._fileName = fileName
        self.loadFile()

    def store(self, pers):
        PersonRepository.store(self, pers)
        self.writeToBinaryFile(PersonRepository.getAllPersons(self))

    def delete(self, pers):
        PersonRepository.delete(self, pers)
        self.writeToBinaryFile(PersonRepository.getAllPersons(self))

    def update(self, person, newPerson):
        PersonRepository.update(self, person, newPerson)
        self.writeToBinaryFile(PersonRepository.getAllPersons(self))

    def writeToBinaryFile(self, persons):
        f = open(self._fileName, "wb")
        pickle.dump(persons, f)
        f.close()

    def readBinaryFile(self):
        try:
            f = open(self._fileName, "rb")
            return pickle.load(f)
        except EOFError:
            print("Cannot open file!")
        except IOError as e:
            print("Cannot open file!" + str(e))

    def loadFile(self):
        for pers in self.readBinaryFile():
            PersonRepository.store(self, pers)