
from domain import*
import copy

def initList():
    l=[{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":2,"Value":140,"Type":"in","Description":"salary"},
       {"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
       {"Day":22,"Value":469,"Type":"in","Description":"salary"},{"Day":25,"Value":32,"Type":"out","Description":"shoes"},
       {"Day":25,"Value":180,"Type":"in","Description":"chocolate"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
       {"Day":28,"Value":74,"Type":"out","Description":"hats"},{"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]
    return l


def undo(l,undoL):
    l=copy.deepcopy(undoL.pop())
    return l,undoL


def findPozToInsert(l,t):
    for poz in range(0,len(l)):
        if getDay(t)<getDay(l[poz]) or getDay(t)== getDay(l[poz]) and getValue(t)<getValue(l[poz]):
            return poz
    return len(l)

def add(l,newValue,newType,newDescription):
    '''
        Adds a new transaction to the list.
        Input:
            -l: list
            -newValue: integer
            -newType: string
            -newDescription: string
        Output:
            -the updated list
    '''
    t={"Day":0,"Value":0,"Type":" ","Description":" "}
    import datetime
    date=datetime.datetime.now()
    day=date.day
    day=int(day)
    setDay(t,day)
    setValue(t,newValue)
    setType(t,newType)
    setDescription(t,newDescription)
    poz=findPozToInsert(l,t)
    l.insert(poz,t)

def insert(l,newDay,newValue,newType,newDescription):
    '''
        Adds a new transaction to the list.
        Input:
            -l: list
            -newDay: integer
            -newValue: integer
            -newType: string
            -newDescription: string
        Output:
            -the updated list
    '''
    t={"Day":0,"Value":0,"Type":" ","Description":" "}
    setDay(t,newDay)
    setValue(t,newValue)
    setType(t,newType)
    setDescription(t,newDescription)
    poz=findPozToInsert(l,t)
    l.insert(poz,t)

'''
     Modify transactions from the list
'''

def removeDay(l,day):
    '''
        Removes all transactions made on a given day from the list.
        Input:
            -l: list
            -day: integer
        Output:
            -the updated list
    '''
    i=0
    while i<len(l):
        if day == getDay(l[i]):
            l.remove(l[i])
        else:
            i+=1
    
def removeInterval(l,startDay,endDay):
    '''
        Removes all transactions made on between two dates from the list.
        Input:
            -l: list
            -startDay: integer
            -endDay: integer
        Output:
            -the updated list
    '''
    if startDay>endDay:
        startDay,endDay=endDay,startDay
    i=0
    while i<len(l):
        if startDay <= getDay(l[i]) and endDay >= getDay(l[i]):
            l.remove(l[i])
        else:
            i+=1

def removeType(l,type_):
    '''
        Removes all transactions of a given type from the list.
        Input:
            -l: list
            -type_: string
        Output:
            -the updated list
    '''
    i=0
    while i<len(l):
        if type_==getType(l[i]):
            l.remove(l[i])
        else:
            i+=1

def replace(l,day,type_,description,newValue):
    '''
        Replaces the values of a transaction with given day,type and description
        Input:
            -l: list
            -day: integer
            -type: string
            -description: string
        Output:
            -the updated list
    '''
    found=False
    i=0
    while not found and i<len(l):
        if getDay(l[i])==day and getType(l[i])==type_ and description==getDescription(l[i]):
            setValue(l[i],newValue)
            found=True
        i+=1
    if not found:
        print("Transaction not found!")

'''
    Write the transactions having different properties
'''
def printTransaction(t,number):
    '''
        Prints a single trasaction
        Input:
            -t: dictionary
            -number: integer
        Output: none
    '''
    print("Transaction " + str(number) + ": ")
    print("Day: " + str(getDay(t)) + ", Value: " + str(getValue(t)) + ", Type: " + str(getType(t)))
    print("Description: " + str(getDescription(t)))
    print()

def printList(l):
    '''
        Prints all the elements of the list
        Input:
            -l: list
        Output:
            -testList: list (used for testing the function)
    '''
    testList=[]
    for i in range(0,len(l)):
        printTransaction(l[i],int(i+1))
        testList.append(l[i])
    return testList

def listType(l,type_):
    '''
        Prints all the elements of the list of a given type
        Input:
            -l: list
            -type_: string
        Output:
            -testList: list (used for testing the function)
    '''
    testList=[]
    for i in range(0,len(l)):
        if type_==getType(l[i]):
            printTransaction(l[i],i+1)
            testList.append(l[i])
    return testList

def listValue(l,sign,value):
    '''
        Prints all the elements of the list that are smaller, bigger or equal to a given value
        Input:
            -l: list
            -sign: string
            -value: integer
        Output:
            -testList: list (used for testing the function)
    '''
    if sign!='<' and sign!='=' and sign!='>':
        print("Invalid sign! Please type <,> or =")
        return
    testList=[]
    for i in range(0,len(l)):
        if sign == "=" and value==getValue(l[i]) or sign=="<" and value>getValue(l[i]) or sign==">" and value<getValue(l[i]):
            printTransaction(l[i],i+1)
            testList.append(l[i])
    return testList
            

def listBalance(l,day):
    '''
        Returns the balance of the account on a given day
        Input:
            -l: list
            -day: integer
        Output:
            -balance: integer
    '''
    balance=0
    for i in range(0,len(l)):
        if day==getDay(l[i]):
            if getType(l[i])=="in":
                balance+=getValue(l[i])
            else:
                balance-=getValue(l[i])
    return balance

'''
    Different characteristics of the transactions
'''

def sumType(l,type_):
    '''
        Returns the sum of the values of all transactions of a given type
        Input:
            -l: list
            -type_: string
        Output:
            -s: integer
    '''
    s=0
    for i in range(0,len(l)):
        if getType(l[i])==type_:
            s+=getValue(l[i])
    return s

def maxDay(l,type_,day):
    '''
        Returns the transaction of a given type, from a given day and with a maximum value
        Input:
            -l: list
            -type: string
            -day: integer
        Output:
            -maxTr: dictionary
            -number: integer
    '''
    maximum=0
    number=0
    maxTr={"Day":0,"Value":0,"Type":" ","Description":" "}
    for i in range(0,len(l)):
        if getType(l[i])==type_ and getDay(l[i])==day and getValue(l[i])>maximum:
            maximum=getValue(l[i])
            maxTr=l[i]
            number=int(i+1)
    return maxTr,number

def filterType(l,type_):
    '''
        Keeps the transactions of a given type
        Input:
            -l: list
            -type_: string
        Output: the updated list
        '''
    i=0
    while i<len(l):
        if type_!=getType(l[i]):
            l.remove(l[i])
        else:
            i+=1

def filterTypeValue(l,type_,value):
    '''
        Keeps the transactions of a given type with a value smaller than the given one
        Input:
            -l: list
            -type_: string
            -value: integer
        Output: the updated list
    '''
    i=0
    value=int(value)
    while i<len(l):
        if type_==getType(l[i]) and getValue(l[i])<value:
            i+=1
        else:
            l.remove(l[i])
            
