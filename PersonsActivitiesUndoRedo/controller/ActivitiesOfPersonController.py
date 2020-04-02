class ActivitiesOfPersonController:
    def __init__(self, actPers):
        self.__actPers = actPers

    def getActivitiesOfPerson(self, persId):
        return self.__actPers.getActivitiesOfPerson(persId)

    def upcomingActivities(self):
        return self.__actPers.upcomingActivities()

    def deleteId(self, persId):
        return self.__actPers.deleteId(persId)

    def addId(self, activities, persId):
        return self.__actPers.addId(activities, persId)
