import datetime

class Task:

    name = ""
    completed = False
    className = ""
    dueDate = None
    doDate = None

    def __init__(self, nameInput, classNameInput, dueDateInput, doDateInput):

        self.name = nameInput
        self.className = classNameInput
        self.dueDateInput = dueDateInput
        self.doDateInput = doDateInput

    def moveDoDateAuto():
        pass

    def markComplete():
        pass