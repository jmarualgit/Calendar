import pandas as pd

# create CSV file
def createCalendar():
    pass

def printCalendar(filepath):
    filepath = "./Files/" + filepath
    df = pd.read_csv(filepath)
    
    print(df.to_string(justify='left', index=False))

def getValue(filepath, row, column):
    filepath = "./Files/" + filepath
    df = pd.read_csv(filepath)
    
    print("Old value: " + str(df.at[row, column]))

# takes a task object
def addTask(filepath, task):
    filepath = "./Files/" + filepath
    df = pd.read_csv(filepath)
    
    df.loc[len(df)] = task
    df.to_csv(filepath, index=False)

def modifyTask(filepath, row, column, newValue):
    filepath = "./Files/" + filepath
    df = pd.read_csv(filepath)
    
    df.at[row, column] = newValue
    df.to_csv(filepath, index=False)

def removeTask(filepath, rowToRemove):
    filepath = './Files/' + filepath
    df = pd.read_csv(filepath)
    
    df = df.drop(index=rowToRemove)
    df.to_csv(filepath, index=False)

def autoSort(filepath):
    filepath = "./Files/" + filepath
    df = pd.read_csv(filepath)
    
    df = df.sort_values(by=["Do Date"])
    
    df.to_csv(filepath, index=False)