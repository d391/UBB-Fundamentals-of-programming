class ActivityValidator:

    def __init__(self, actRepo, persRepo):
        self.__actRepo = actRepo
        self.__persRepo = persRepo

    def overlap(self, activity):
        for act in self.__actRepo.getAll():
            if act.date == activity.date and act.time == activity.time:
                return False
        return True

    def validateId(self, activity):
        for act in self.__actRepo.getAllActivities():
            if act.activityId == activity.id:
                return False
        return True

    def validateTimeDate(self, year, month, day, time):
        return time < "00:00" or time > "24:00" or year < 2017 or month < 0 or month > 12 or day < 1 or day > 31

    def verifyIds(self, persIds):
        for id in persIds:
            if self.__persRepo.find(id) != None:
                return True
        return False

    def validate(self, activity):
        errors = []
        if activity.activityId == "" or activity.description == "" or activity.time == "":
            errors.append(" Void field(s)")
        if self.overlap(activity) == False:
            errors.append(" This activity overlaps with another one!")
        if activity.activityId < 1 or type(activity.activityId) != int:
            errors.append(" Invalid id! Id must be a positive integer")
        if len(activity.personIds) < 1:
            errors.append(" Invalid number of persons!")
        if self.verifyIds(activity.personIds) == False:
            errors.append(" Id of participant not in the list!")
        return errors
