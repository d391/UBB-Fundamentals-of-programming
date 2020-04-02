from domain.Activity import *
from datetime import date
from controller.UndoController import Function
from controller.UndoController import Operation


class ActivityController:
    def __init__(self, repo, validator, undoController):
        self.__repo = repo
        self.__validator = validator
        self.__undoController = undoController

    def create(self, actId, persIds, year, month, day, time, description):
        if self.__validator.validateTimeDate(year, month, day, time) == True:
            activity = Activity(actId, persIds, date(2018, 3, 12), time, description)
            errors = self.__validator.validate(activity)
            errors.append(" Invalid time or date!")
        else:
            date_ = date(year, month, day)
            activity = Activity(actId, persIds, date_, time, description)
            errors = self.__validator.validate(activity)
        if len(errors) == 0:
            f1 = Function(self.__repo.delete, activity)
            f2 = Function(self.__repo.store, activity)
            o = Operation(f1, f2)
            self.__undoController.addOperation(o)
            self.__repo.store(activity)
            return activity
        else:
            return errors

    def delete(self, id):
        act = self.find(id)
        if act != None:
            f1 = Function(self.__repo.store, act)
            f2 = Function(self.__repo.delete, act)
            o = Operation(f1, f2)
            self.__undoController.addOperation(o)
            return self.__repo.delete(act)
        else:
            return "Activity not found!"

    def find(self, id):
        return self.__repo.find(id)

    def update(self, activity, newPersIds, newYear, newMonth, newDay, newTime, newDescr):
        if self.__validator.validateTimeDate(newYear, newMonth, newDay, newTime) == True:
            newActivity = Activity(activity.activityId, newPersIds, date(2018, 3, 12), newTime, newDescr)
            errors = self.__validator.validate(newActivity)
            errors.append(" Invalid time or date!")
        else:
            newDate = date(newYear, newMonth, newDay)
            newActivity = Activity(activity.activityId, newPersIds, newDate, newTime, newDescr)
            auxActivity = Activity(activity.activityId, activity.personIds, activity.date, activity.time, activity.description)
            errors = self.__validator.validate(newActivity)
            if len(errors) == 0:
                f1 = Function(self.__repo.update, newActivity, auxActivity)
                f2 = Function(self.__repo.update, auxActivity, newActivity)
                o = Operation(f1, f2)
                self.__undoController.addOperation(o)
                return self.__repo.update(activity, newActivity)
        return errors

    def search(self, choice):
        return self.__repo.search(choice)

    def givenDay(self, date_):
        return self.__repo.givenDay(date_)

    def list(self):
        return str(self.__repo)
