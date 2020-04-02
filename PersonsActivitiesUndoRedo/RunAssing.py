from ui import UI
from repository.ActivityRepository import ActivityRepository
from repository.ActivityRepository import ActivityTextFileRepo
from repository.ActivityRepository import ActivityBinaryRepo
from repository.PersonRepository import PersonTextFileRepo
from repository.PersonRepository import PersonBinaryRepo
from repository.PersonRepository import PersonRepository
from repository.DayRepository import DayRepository
from domain.PersonValidator import PersonValidator
from domain.ActivityValidator import ActivityValidator
from repository.ActivitiesOfPerson import ActivitiesOfPerson
from controller.ActivityController import ActivityController
from controller.PersonController import PersonController
from controller.DayController import DayController
from controller.ActivitiesOfPersonController import ActivitiesOfPersonController
from controller.UndoController import UndoController
from domain.Generators import initListPers
from domain.Generators import initListActs


def readSettings():
    settings = []
    f = open("settings.properties", "r")
    s = f.read()
    lines = s.split("\n")
    set = {}
    l = 0
    for line in lines:
        tokens = line.split("=")
        set[tokens[0].strip()] = tokens[1].strip()
        settings.append(set)
        l += 1
    return settings


settings = readSettings()
if settings[0]["file_type"] == "memory":
    persRepo = PersonRepository()
    initListPers(persRepo)
if settings[0]["file_type"] == "text_file":
    persRepo = PersonTextFileRepo()
if settings[0]["file_type"] == "binary_file":
    persRepo = PersonBinaryRepo()

if settings[1]["file_type"] == "memory":
    actRepo = ActivityRepository()
    initListActs(actRepo)
if settings[1]["file_type"] == "text_file":
    actRepo = ActivityTextFileRepo()
if settings[1]["file_type"] == "binary_file":
    actRepo = ActivityBinaryRepo()


dayRepo = DayRepository()
#initListGen(persRepo)
#initListGenAct(persRepo, actRepo)
actPers = ActivitiesOfPerson(persRepo, actRepo)
dayController = DayController(dayRepo, actRepo)
persValidator = PersonValidator(persRepo)
actValidator = ActivityValidator(actRepo, persRepo)
undoController = UndoController()
actPersController = ActivitiesOfPersonController(actPers)
persController = PersonController(persRepo, persValidator, actPersController, undoController)
actController = ActivityController(actRepo, actValidator, undoController)
assign = UI(persController, actController, dayController, actPersController, undoController)

assign.run()

