class Person:
    def __init__(self, id, name, phoneNr, address):
        self._id = id
        self._name = name
        self._phoneNr = phoneNr
        self._address = address

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def phoneNumber(self):
        return self._phoneNr

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, newName):
        self._name = newName

    @phoneNumber.setter
    def phoneNumber(self, newPhoneNr):
        self._phoneNr = newPhoneNr

    @address.setter
    def address(self, newAddress):
        self._address = newAddress

    def __str__(self):
        return "Id: " + str(self._id) + "\n Name: " + self._name + "\n Phone number: " + self._phoneNr + "\n Address: " + self._address + "\n"

