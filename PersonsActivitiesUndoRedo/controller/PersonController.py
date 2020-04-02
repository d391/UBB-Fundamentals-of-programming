from domain.Person import *
from controller.UndoController import *


class PersonController:
    def __init__(self, repo, validator, actPers, undoController):
        self.__repo = repo
        self.__validator = validator
        self.__actPers = actPers
        self.__undoController = undoController

    def create(self, id, name, phoneNr, address):
        person = Person(id, name, phoneNr, address)
        errors = self.__validator.validate(person)
        if self.__validator.alreadyStored(person) == True:
            errors.append(" Person already stored or id already used!")
        if len(errors) == 0:
            self.__repo.store(person)
            f1 = Function(self.__repo.delete, person)
            f2 = Function(self.__repo.store, person)
            o = Operation(f1, f2)
            self.__undoController.addOperation(o)
            return person
        return errors

    def delete(self, id):
        pers = self.find(id)
        if pers != None:
            deleteCascade = CascadeOperation()
            f1 = Function(self.__repo.store, pers)
            f2 = Function(self.__repo.delete, pers)
            o = Operation(f1, f2)
            deleteCascade.add(o)
            f1 = Function(self.__actPers.deleteId, pers.id)
            activities = self.__actPers.getActivitiesOfPerson(pers.id)
            f2 = Function(self.__actPers.addId, activities, pers.id)
            o = Operation(f2, f1)
            deleteCascade.add(o)
            self.__undoController.addOperation(deleteCascade)
            return self.__repo.delete(pers)
        else:
            return "Person not found!"

    def find(self, id):
        return self.__repo.find(id)

    def update(self, person, newName, newPhoneNr, newAddress):
        newPerson = Person(person.id, newName, newPhoneNr, newAddress)
        auxPerson = Person(person.id, person.name, person.phoneNumber, person.address)  #???
        errors = self.__validator.validate(newPerson)
        if len(errors) == 0:
            f1 = Function(self.__repo.update, newPerson, auxPerson)
            f2 = Function(self.__repo.update, auxPerson, newPerson)
            o = Operation(f1, f2)
            self.__undoController.addOperation(o)
            return self.__repo.update(person, newPerson)
        else:
            return errors

    def search(self, choice):
        return self.__repo.search(choice)

    def list(self):
        return str(self.__repo)
