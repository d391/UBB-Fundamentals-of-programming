class PersonValidator:
    def __init__(self, personRepo):
        self.__personRepo = personRepo

    def alreadyStored(self, person):
        for pers in self.__personRepo.getAllPersons():
            if pers.id == person.id:
                return True
        return False

    def validate(self, person):
        errors = []
        if person.id == "" or person.phoneNumber == "" or person.address == "" or person.name == "":
            errors.append(" Empty fields!")
        if type(person.id) != int or person.id <= 0:
            errors.append(" Invalid id! Please introduce a positive integer!")
        if person.name[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            errors. append(" Name must start with a capital letter!")
        if len(person.phoneNumber) != 10:
            errors.append(" Invalid phone number!")
        return errors
