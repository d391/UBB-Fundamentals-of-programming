from domain.Activity import *
from datetime import date
import copy
from repository.PersonRepository import *
from SortFilter import filter
from SortFilter import gnomeSort
from domain.Iterable import Iterable
from domain.Generators import initListGenAct


def sameDate(act, date_):
    return act.date == date_


def cmpByTime(act1, act2):
    if act1.time < act2.time:
        return True
    return False


class ActivityRepository:
    def __init__(self):
        self.__actRepo = Iterable()

    def store(self, activity):
        """
        Adds a new activity to the repository
        Input:
            - activity: Activity
        Output:
            - updated version of the repository
        """
        self.__actRepo.append(activity)

    def find(self, actId):
        """
        Searches for and returns an activity using its id
        Input:
            - actId: integer
        Output:
            - act: Activity (if it is found)
            - None, otherwise
        """
        for act in self.__actRepo:
            if actId == act.activityId:
                return act
        return None

    def update(self, activity, newActivity):
        """
        Updates the data of an activity
        Input:
            - act: Activity
            - persIds: list
            - date: date
            - time: string
            - description: string
        Output:
            - updated version of act
        """
        for act in self.__actRepo:
            if act.activityId == activity.activityId:
                act.personIds = copy.deepcopy(newActivity.personIds)
                act.date = newActivity.date
                act.time = newActivity.time
                act.description = newActivity.description
                return act

    def delete(self, act):
        """
        Removes an activity from the repository
        Input:
            - act: Activity
        Output:
            - updated version of the repository
        """
        self.__actRepo.remove(act)

    def getAll(self):
        """
        Return all the elements of the repository
        Input: -
        Output:
            - actRepo: repository
        """
        return self.__actRepo.list

    def search(self, choice):
        """
        Returns all the activities that have the given criteria
        Input:
            - choice: string
        Output:
            - results: list
        """
        results = []
        for act in self.__actRepo:
            if choice in act.time[0:] or choice in act.description[0:] or choice in str(act.date)[0:]:
                results.append(act)
        return results

    def findPoz(self, results, time_):
        """
        Returns the insertion position so that the result list will remain ordered
        Input:
            - results: list
            - time: string
        Output:
            - poz: integer
        """
        poz = 0
        for act in results:
            if act.time > time_:
                return poz
            poz += 1
        return poz

    def givenDay(self, date_):
        """
        Returns all the activites that take place on a given day
        Input:
            - date_: date
        Output:
            - results: list
        """
        results = filter(self.__actRepo, sameDate, date_)
        gnomeSort(results, cmpByTime)
        return results

    def __str__(self):
        """
        String format of the activity repository
        Input: -
        Output:
            - text: string
        """
        text = ""
        for act in self.__actRepo:
            text += str(act)
            text += "\n"
        return text


class ActivityTextFileRepo(ActivityRepository):

    def __init__(self, fileName = "activities.txt"):
        ActivityRepository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def store(self, act):
        ActivityRepository.store(self, act)
        self._saveFile()

    def delete(self, act):
        ActivityRepository.delete(self, act)
        self._saveFile()

    def update(self, act, newAct):
        PersonRepository.update(self, act, newAct)
        self._saveFile()

    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for act in self.getAll():
                f.write(str(act.activityId) + "          " + str(act.personIds) + "          " + str(act.date) + "          " + act.time + "          "  + act.description + "\n")
        except IOError as e:
            print("Cannot load file" + str(e))
        finally:
            f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline()
            while len(line) > 2:
                tok = line.split("          ")
                tokDate = tok[2].split("-")
                tok[1] = readList(tok[1])
                act = Activity(int(tok[0].strip()), tok[1], date(int(tokDate[0]), int(tokDate[1]), int(tokDate[2])), tok[3], tok[4].strip())
                ActivityRepository.store(self, act)
                line = f.readline()
        except IOError as e:
            print("Cannot load file" + str(e))
        finally:
            f.close()


class ActivityBinaryRepo(ActivityRepository):

    def __init__(self, fileName = "activities.pickle"):
        ActivityRepository.__init__(self)
        self._fileName = fileName
        self.loadFile()

    def store(self, act):
        ActivityRepository.store(self, act)
        self.writeToBinaryFile(ActivityRepository.getAll(self))

    def delete(self, act):
        ActivityRepository.delete(self, act)
        self.writeToBinaryFile(ActivityRepository.getAll(self))

    def update(self, act, newAct):
        ActivityRepository.update(self, act, newAct)
        self.writeToBinaryFile(ActivityRepository.getAll(self))

    def writeToBinaryFile(self, activities):
        f = open(self._fileName, "wb")
        pickle.dump(activities, f)
        f.close()

    def readBinaryFile(self):
        try:
            f = open(self._fileName, "rb")
            return pickle.load(f)
        except EOFError:
            print("Cannot open file!")
        except IOError as e:
            print("Cannot open file!" + str(e))

    def loadFile(self):
        for act in self.readBinaryFile():
            ActivityRepository.store(self, act)


def readList(strList):
    list = []
    number = 0
    for cr in strList:
        if cr not in [",", " ", "[", "]"]:
            number = number*10 + int(cr)
        elif number != 0:
            list.append(number)
            number = 0
    return list

