class Activity:
    def __init__(self, actId, persIds, date, time, description):
        self._actId = actId
        self._persIds = persIds
        self._date = date
        self._time = time
        self._description = description

    @property
    def activityId(self):
        return self._actId

    @property
    def personIds(self):
        return self._persIds

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def description(self):
        return self._description

    @personIds.setter
    def personIds(self, newPersonsId):
        self._persIds = newPersonsId

    @date.setter
    def date(self, newDate):
        self._date = newDate

    @time.setter
    def time(self, newTime):
        self._time = newTime

    @description.setter
    def description(self, newDescr):
        self._description = newDescr

    def __str__(self):
        text = "Activity ID: " + str(self._actId) + "\n Persons IDs: "
        for id in self._persIds:
            text += (str(id) + " ")
        text += "\n Date: " + str(self._date) + "\n Time: " + self._time + "\n Description: " + self._description + "\n"
        return text
