import Calendar
import os
import datetime

path = ".//Files"

for i, item in enumerate(os.listdir(path)):
   print(str(i + 1) + ": " + item)

calendar = input("Type calendar # to open and press enter\n")

# set file name as calendar
calendar = os.listdir(path)[int(calendar) - 1]
Calendar.printCalendar(calendar)

choice = input("\nWhat would you like to do?\n1: Add task\n2: Modify task\n3: Delete task\n4: Exit\n")

match choice:
    case "1":
        taskName = input("Task Name:\n")
        className = input("Class Name:\n")
        dueDateInput = datetime.date.fromisoformat(input("Due Date: (YYYYMMDD)\n"))
        doDateInput = datetime.date.fromisoformat(input("Do Date: (YYYYMMDD)\n"))
        
        newTask = [taskName, className, dueDateInput, doDateInput, False]
        
        Calendar.addTask(calendar, newTask)
        Calendar.autoSort(calendar)
    
    case "2":
        taskNum = int(input("\nSelect task number\n"))
        columnInput = input("\nSelect column\n")
        
        if (columnInput == "Due Date" or columnInput == "Do Date"):
            newValue = datetime.date.fromisoformat(input("\nWhat is the new value?\n"))
        else:
            newValue = input("\nWhat's the new value?\n")
        
        Calendar.getValue(calendar, taskNum, columnInput)
        
        Calendar.modifyTask(calendar, taskNum, columnInput, str(newValue))
        Calendar.autoSort(calendar)
        
    case "3":
        rowToRemove = int(input("\nSelect row to remove\n"))
        Calendar.removeTask(calendar, rowToRemove)
        
    case "4":
        pass
        
Calendar.printCalendar(calendar)