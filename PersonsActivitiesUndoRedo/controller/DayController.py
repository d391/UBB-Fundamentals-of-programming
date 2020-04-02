class DayController:
    def __init__(self, dayRepo, actRepo):
        self.__dayRepo = dayRepo
        self.__actRepo = actRepo

    def storeDays(self):
        return self.__dayRepo.storeDays(self.__actRepo)

    def printDays(self):
        return str(self.__dayRepo)
