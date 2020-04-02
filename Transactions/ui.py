'''
    Main
'''

from operations import*


def menuUI():
    print("To add a transaction to the current day, type:  add <value> <type> <description>")
    print("To insert a transaction in any day you want, type: insert <day> <value> <type> <description>")
    print("To remove all transactions from a given day, type: remove <day>")
    print("To remove all transactions between two dates, type: remove <start day> to <end day>")
    print("To remove all transactions of a given type, type: remove <type>")
    print("To replace the value from a transaction of a given day, type and description, type: replace <day> <type> <description> with <value>")
    print("To see all the transactions, type: list")
    print("To see all the transactions of a given type, type: list <type>")
    print("To see all the transactions whose value is bigger, type: list > <value>; smaller, type: list < <value>; or equal to a given value, type: list = <value>")
    print("To compute the account's balance on a given day, type: list balance <day>")
    print("To see the sum of the values of all transactions of a given type, type: sum <type>")
    print("To see the maximum transaction on a given day and type, type: max <type> <day>")
    print("To keep only the transactions of a given type, type: filter <type>")
    print("To keep only the transaction of a given type and with a smaller value than a given one, type: filter <type> <value>")
    print("To exit the program, type: x")
    print()

def validateDay(day):
    try:
        day=int(day)
    except:
        print("The day number must be an integer")
        return False
    if day<1 or day>30:
        print("Invalid day number! Please type a number between 1 and 30")
        return False
    return True

def validateType(type_):
    if type_!='in' and type_!='out':
        print("Invalid type! Please type 'in' or 'out'")
        return False
    return True

def validateValue(value):
    try:
        value=int(value)
    except:
        print("The value number must be an integer")
        return False
    if value<0:
        print("Invalid value! Please type a positive value")
        return False
    return True

def dataValidation(day,value,type_):
    if validateType(type_) == False or validateValue(value) == False or validateDay(day)==False:
        return False
    return True


def removeUI(l,command):
    if len(l)==0:
        print("You have no transactions!")
    elif len(command)==2:
        if command[1]!="in" and command[1]!="out":
            if validateDay(command[1]) == True:
                command[1]=int(command[1])
                removeDay(l,command[1])
        else:
            if validateType(command[1]) == True:
                removeType(l,command[1])
    else:
        startDay=command[1]
        endDay=command[3]
        if validateDay(startDay)==False or validateDay(endDay)==False:
            return
        startDay=int(startDay)
        endDay=int(endDay)
        removeInterval(l,startDay,endDay)


def listUI(l,command):
    if len(l)==0:
        print("You have no transactions!")
    elif len(command)==1:
        printList(l)
    elif len(command)==2:
        if validateType(command[1]) == True:
            listType(l,command[1])
    elif len(command)==3:
        if command[1]=="balance":
            if validateDay(command[2]) == True:
                command[2]=int(command[2])
                balance=listBalance(l,command[2])
                print("The balance for day " + str(command[2]) + " is: " + str(balance))
        else:
            if validateValue(command[2]) == True:
                command[2]=int(command[2])
                listValue(l,command[1],command[2])


def filterUI(l,command):
    if len(command)==3:
        if dataValidation(1,command[2],command[1]) == True:
            command[2]=int(command[2])
            filterTypeValue(l,command[1],command[2])
    else:
        if validateType(command[1]) == True:
            filterType(l,command[1])



def main():
    print("WELCOME TO YOUR BANK ACCOUNT")
    l=initList()
    undoL=[[]]
    while True:
        try:
            print("To open the command menu, type: menu")
            command=input("Type command: ").lower()
            command=command.split()
            if command[0]=="menu":
                menuUI()
            elif command[0] == "add":
                if dataValidation(1,command[1],command[2]) == True:
                    auxL = copy.deepcopy(l)
                    undoL.append(auxL)
                    command[1]=int(command[1])
                    add(l,command[1],command[2],command[3])
            elif command[0]=="insert":
                if dataValidation(command[1], command[2],command[3]) == True:
                    auxL = copy.deepcopy(l)
                    undoL.append(auxL)
                    command[1]=int(command[1])
                    command[2]=int(command[2])
                    insert(l,command[1],command[2],command[3],command[4])
            elif command[0]=="remove":
                auxL = copy.deepcopy(l)
                undoL.append(auxL)
                removeUI(l,command)
            elif command[0]=="replace":
                if dataValidation(command[1],command[5],command[2]) == True:
                    auxL = copy.deepcopy(l)
                    undoL.append(auxL)
                    command[1]=int(command[1])
                    command[5]=int(command[5])
                    replace(l,command[1],command[2],command[3],command[5])
            elif command[0]=="list":
                listUI(l,command)
            elif command[0]=="sum":
                if validateType(command[1]) == True:
                    s=sumType(l,command[1])
                    print("The sum of all the " + command[1] + " transactions is " + str(s))
            elif command[0]=="max":
                if dataValidation(command[2],1,command[1]) == True:
                    command[2]=int(command[2])
                    maxTr,number=maxDay(l,command[1],command[2])
                    if number == 0:
                        print("No " + command[1] + " transaction found on day " + str(command[2]) + "!")
                    else:
                        printTransaction(maxTr,number)
            elif command[0]=="filter":
                auxL = copy.deepcopy(l)
                undoL.append(auxL)
                filterUI(l,command)
            elif command[0]=="undo":
                if len(undoL)>1:
                    l,undoL=undo(l,undoL)
                else:
                    print("No more undos!")
            elif command[0] == "x":
                return
            else:
                print("Invalid command!")
        except:
            print("The command needs more specifications!")

