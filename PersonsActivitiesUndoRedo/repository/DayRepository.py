from domain.Day import *


class DayRepository:
    def __init__(self):
        self._repo = []

    def findPoz(self, insDay):
        """
        Returns the insertion position so that the list remains ordered
        Input:
            - insDay: Day
        Output:
            - poz: integer
        """
        poz = 0
        for day in self._repo:
            if insDay.numberOfActivities > day.numberOfActivities or insDay.numberOfActivities == day.numberOfActivities and insDay.date > day.date:
                return poz
            poz += 1
        return poz

    def alreadyStored(self, date_):
        """
        Verifies if a date has already been stored in the repo in order to avoid duplications
        Input:
            - date_: date
        Output:
             - True: if it has been already stored
             - False, otherwise
        """
        for day in self._repo:
            if day.date == date_:
                return True
        return False

    def storeDays(self, actRepo):
        """
        Stores all the days in descending order by the number of activities that take place during said days
        Input:
            - actRepo: repository of activities
        Output:
            - repo: repository of days
        """
        for act in actRepo.getAll():
            if self.alreadyStored(act.date) == False:
                day = Day(act.date, 0)
                day.setNumberOfActivities(day.getNumberOfActivities(actRepo))
                poz = self.findPoz(day)
                self._repo.insert(poz, day)
        return self._repo

    def getDays(self):
        """
        Returns all the elements of the repository
        Input: -
        Output:
            - repo: day repository
        """
        return self._repo

    def __str__(self):
        """
        String format of day
        Output:
            - text: string
        """
        text = ""
        for day in self._repo:
            text += str(day)
            text += "\n"
        return text
