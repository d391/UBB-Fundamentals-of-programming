class Day:
    def __init__(self, date, nrActivities):
        self._nrActivities = nrActivities
        self._date = date

    def nameOfMonth(self, month):
        if month == 1:
            return "January"
        if month == 2:
            return "February"
        if month == 3:
            return "March"
        if month == 4:
            return "April"
        if month == 5:
            return "May"
        if month == 6:
            return "June"
        if month == 7:
            return "July"
        if month == 8:
            return "August"
        if month == 9:
            return "September"
        if month == 10:
            return "October"
        if month == 11:
            return "November"
        if month == 12:
            return "December"

    @property
    def date(self):
        return self._date

    @property
    def numberOfActivities(self):
        return self._nrActivities

    def setNumberOfActivities(self, number):
        self._nrActivities = number

    def getNumberOfActivities(self, actRepo):
        number = 0
        for act in actRepo.getAll():
            if self._date == act.date:
                number += 1
        return number

    def __str__(self):
        return "Day: " + str(self._date.day) + " of " + self.nameOfMonth(self._date.month) + " " + str(self._date.year) + "\n Number of activities: " + str(self._nrActivities) + "\n"

