from SortFilter import filter


def idInActList(act, id):
    if id in act.personIds:
        return True
    return False


class ActivitiesOfPerson:
    def __init__(self, persRepo, actRepo):
        self.__persRepo = persRepo
        self.__actRepo = actRepo

    def getActivitiesOfPerson(self, persId):
        '''
        Returns a list of all the activities where a person participates
        Input:
            - persId: integer
        Output:
            - results: list
        '''

        results = filter(self.__actRepo.getAll(), idInActList, persId)
        return results

    def findPoz(self, insPers, results):
        '''
        Finds the insertion position so that the list of activities remains sorted
        Input:
            - insPers: Person
            - results: list
        Output:
            - poz: integer
        '''
        poz = 0
        for pers in results:
            if len(self.getActivitiesOfPerson(pers.id)) < len(self.getActivitiesOfPerson(insPers.id)):
                return poz
            poz += 1
        return poz

    def upcomingActivities(self):
        """
        Returns the list of the persons sorted descending by the number of activities they participate in
        Input : -
        Output:
            -results: list
            -actNumber: list of integers (represents the number of activities each person participates in)
        """
        results = []
        actNumber = []
        for pers in self.__persRepo.getAllPersons():
            poz = self.findPoz(pers, results)
            results.insert(poz, pers)
            actNumber.insert(poz, len(self.getActivitiesOfPerson(pers.id)))
        return results, actNumber

    def deleteId(self, persId):
        """
        If a person is deleted from the address book, this function will delete their id from the activities they were supposed to participate in
        Input:
            - persId: integer
        Output:
            - updated version of the activity repository
        """
        for act in self.__actRepo.getAll():
            if persId in act.personIds:
                act.personIds.remove(persId)

    def addId(self, activities, persId):
        for act in self.__actRepo.getAll():
            for prevAct in activities:
                if act.activityId == prevAct.activityId:
                    act.personIds.append(persId)
                    break
