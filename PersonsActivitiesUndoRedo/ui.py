from datetime import date


class UI:

    def __init__(self, persController, actController, dayController, actPersController, undoController):
        self.__persController = persController
        self.__actController = actController
        self.__dayController = dayController
        self.__actPersController = actPersController
        self.__undoController = undoController

    def menu(self):
        print("Type:")
        print(" ap - to add a person")
        print(" aa - to add an activity")
        print(" rp - to remove a person")
        print(" ra - to remove an activity")
        print(" up - to update the informations of a person")
        print(" ua - to update the informations of an activity")
        print(" sp - to search a person by name or phone number")
        print(" sa - to search an activity by date, time or description")
        print(" lp - to view all the persons")
        print(" la - to view all the activities")
        print(" stsd - to view all the activities on a given day")
        print(" stsbd - to view the list of upcoming activities sorted in descending order by the number of activities on that day")
        print(" stsap - to view all the activities of a given person")
        print(" stsua - to view all the persons in the address book sorted in descending order by the number of activities they participate in")
        print(" u - to undo an operation")
        print(" r - to redo an operation")
        print(" x - to exit")
        print("")

    def printResults(self, results):
        if results == None or results == True:
            print("Operation complete!")
        elif results == False:
            print("No more undos or redos!")
        elif type(results) == str:
            print(results)
        elif type(results) != list:
            print(str(results))
        elif results != []:
            for object in results:
                print(str(object))
            print()
        else:
            print("Nothing found!")

    def addPersUI(self):
        persId = int(input("Give id: "))
        persName = input("Give name: ")
        phoneNr = input("Give phone number: ")
        address = input("Give address: ")
        self.printResults(self.__persController.create(persId, persName, phoneNr, address))

    def addActUI(self):
        actId = int(input("Give id: "))
        number = int(input("Give the number of persons that participate: "))
        persIds = []
        for i in range(number):
            id = int(input("Give id of person number " + str(i+1) + ": "))
            persIds.append(id)
        year = int(input("Give year: "))
        month = int(input("Give month: "))
        day = int(input("Give day: "))
        time = input("Give time: ")
        descr = input("Give description: ")
        results = self.__actController.create(actId, persIds, year, month, day, time, descr)
        self.printResults(results)

    def removePersUI(self):
        persId = int(input("Give id: "))
        self.printResults(self.__persController.delete(persId))
        self.__actPersController.deleteId(persId)

    def removeActUI(self):
        actId = int(input("Give id: "))
        self.printResults(self.__actController.delete(actId))

    def updatePersUI(self):
        persId = int(input("Give id: "))
        pers = self.__persController.find(persId)
        if pers == None:
            print("Id not found!")
            return
        newName = input("Give new name: ")
        newPhoneNr = input("Give new phone number: ")
        newAddress = input("Give new address: ")
        self.printResults(self.__persController.update(pers, newName, newPhoneNr, newAddress))

    def updateActUI(self):
        actId = int(input("Give id: "))
        act = self.__actController.find(actId)
        if act == None:
            print("Id not found!")
            return
        number = int(input("Give the number of participants: "))
        newPersIds = []
        for i in range(number):
            newId = int(input("Give new person id number " + str(i+1) + ": "))
            newPersIds.append(newId)
        try:
            newYear = int(input("Give new year: "))
            newMonth = int(input("Give new month: "))
            newDay = int(input("Give new day: "))
        except:
            newDay = 0
            newMonth = 0
            newYear = 0
        newTime = input("Give new time: ")
        newDescr = input("Give new description: ")
        self.printResults(self.__actController.update(act, newPersIds, newYear, newMonth, newDay, newTime, newDescr))

    def listPersUI(self):
        self.printResults(self.__persController.list())

    def listActUI(self):
        self.printResults(self.__actController.list())

    def searchPersUI(self):
        choice = input("Give the name or the phone number of the person: ")
        results = self.__persController.search(choice)
        if results == []:
            print("Nothing found!")
        else:
            self.printResults(results)

    def searchActUI(self):
        choice = input("Give the date, time or description of the activity: ")
        results = self.__actController.search(choice)
        self.printResults(results)

    def listDayUI(self):
        year = int(input("Give year: "))
        month = int(input("Give month: "))
        day = int(input("Give day: "))
        try:
            date_ = date(year, month, day)
        except:
            print("Invalid date!")
            return
        self.printResults(self.__actController.givenDay(date_))

    def busyDaysUI(self):
        self.__dayController.storeDays()
        self.printResults(self.__dayController.printDays())

    def activityPersonUI(self):
        persId = int(input("Give id: "))
        results = self.__actPersController.getActivitiesOfPerson(persId)
        self.printResults(results)

    def upcomingActivitiesUI(self):
        results, actNumber = self.__actPersController.upcomingActivities()
        ind = 0
        for result in results:
            print(str(result) + " Number of activities: " + str(actNumber[ind]))
            print()
            ind += 1

    def undoUI(self):
        self.printResults(self.__undoController.undo())

    def redoUI(self):
        self.printResults(self.__undoController.redo())

    def run(self):
        commandDict = {"aa": self.addActUI, "ra": self.removeActUI, "ua": self.updateActUI, "la": self.listActUI, "sa": self.searchActUI, "stsd": self.listDayUI, "stsbd": self.busyDaysUI, "ap": self.addPersUI, "rp": self.removePersUI, "up": self.updatePersUI, "lp": self.listPersUI, "sp": self.searchPersUI, "stsb": self.busyDaysUI, "stsap": self.activityPersonUI, "stsua": self.upcomingActivitiesUI, "u": self.undoUI, "r": self.redoUI}
        while True:
            self.menu()
            command = input("Type command: ")
            if command in commandDict.keys():
                commandDict[command]()
            elif command == "x":
                return
            else:
                print("Invalid command!")
