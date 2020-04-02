from operations import *

'''l=[{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":2,"Value":140,"Type":"in","Description":"salary"},
       {"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
       {"Day":22,"Value":469,"Type":"in","Description":"salary"},{"Day":25,"Value":32,"Type":"out","Description":"shoes"},
       {"Day":25,"Value":180,"Type":"in","Description":"chocolate"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
       {"Day":28,"Value":74,"Type":"out","Description":"hats"},{"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]'''


def testRemoveInterval():
    l=initList()
    removeInterval(l,8,25)
    assert l == [{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":2,"Value":140,"Type":"in","Description":"salary"},
       {"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
       {"Day":28,"Value":74,"Type":"out","Description":"hats"},{"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]
    l = initList()
    removeInterval(l, 30, 1)
    assert l == []


def testAdd():
    l=[]
    add(l,9999,"in","description")
    print(l)
    assert l == [{"Day":31,"Value":9999,"Type":"in","Description":"description"}]
    add(l,1000,"in","pizza")
    assert l == [{"Day":31,"Value":1000,"Type":"in","Description":"pizza"},{"Day":31,"Value":9999,"Type":"in","Description":"description"}]


def testInsert():
    l = []
    insert(l, 30, 9999, "in", "description")
    assert l == [{"Day": 30, "Value": 9999, "Type": "in", "Description": "description"}]
    insert(l,12,100,"out","salary")
    assert l == [{"Day": 12, "Value": 100, "Type": "out", "Description": "salary"},{"Day": 30, "Value": 9999, "Type": "in", "Description": "description"}]


def testRemoveDay():
    l=initList()
    removeDay(l,2)
    assert l == [{"Day":13,"Value":70,"Type":"out","Description":"donuts"},{"Day":22,"Value":469,"Type":"in","Description":"salary"},
                 {"Day":25,"Value":32,"Type":"out","Description":"shoes"},{"Day":25,"Value":180,"Type":"in","Description":"chocolate"},
                 {"Day":28,"Value":66,"Type":"in","Description":"salary"},{"Day":28,"Value":74,"Type":"out","Description":"hats"},
                 {"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]
    removeDay(l,28)
    assert l == [{"Day":13,"Value":70,"Type":"out","Description":"donuts"},{"Day":22,"Value":469,"Type":"in","Description":"salary"},
                 {"Day":25,"Value":32,"Type":"out","Description":"shoes"},{"Day":25,"Value":180,"Type":"in","Description":"chocolate"},
                 {"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]


def testRemoveType():
    l=initList()
    removeType(l,"in")
    assert l == [{"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
                 {"Day": 25, "Value": 32, "Type": "out", "Description": "shoes"},{"Day":28,"Value":74,"Type":"out","Description":"hats"},
                 {"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]
    removeType(l,"out")
    assert l == []


def testReplace():
    l=[{"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"}]
    replace(l,2,"out","clothes",9999)
    assert l == [{"Day":2,"Value":9999,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"}]
    replace(l,13,"out","donuts",9999)
    assert l == [{"Day":2,"Value":9999,"Type":"out","Description":"clothes"},{"Day":13,"Value":9999,"Type":"out","Description":"donuts"}]


def testPrintList():
    l=initList()
    tl=printList(l)
    assert l == tl


def testListType():
    l=initList()
    tl=listType(l,"out")
    assert tl == [{"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
                 {"Day": 25, "Value": 32, "Type": "out", "Description": "shoes"},{"Day":28,"Value":74,"Type":"out","Description":"hats"},
                 {"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]


def testListValue():
    l=initList()
    tl=listValue(l,"<",100)
    assert tl == [{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
                  {"Day": 25, "Value": 32, "Type": "out", "Description": "shoes"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
                  {"Day": 28, "Value": 74, "Type": "out", "Description": "hats"}]


def testListBalance():
    l=initList()
    balance=listBalance(l,2)
    assert balance == 2
    balance=listBalance(l,28)
    assert balance == -8


def testSum():
    l=initList()
    sum=sumType(l,"in")
    assert sum == 915
    sum=sumType(l,"out")
    assert sum == 564


def testMax():
    l=initList()
    maxx,number=maxDay(l,"in",2)
    assert maxx == {"Day":2,"Value":140,"Type":"in","Description":"salary"} and number == 2
    maxx,number=maxDay(l,"out",28)
    assert maxx == {"Day":28,"Value":74,"Type":"out","Description":"hats"} and number == 9
    maxx,number=maxDay(l,"in",1)
    assert maxx == {"Day":0,"Value":0,"Type":" ","Description":" "} and number==0


def testFilterType():
    l=initList()
    filterType(l,"out")
    assert l == [{"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
                 {"Day": 25, "Value": 32, "Type": "out", "Description": "shoes"},{"Day":28,"Value":74,"Type":"out","Description":"hats"},
                 {"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]
    filterType(l,"in")
    assert l == []


def testFilterTypeValue():
    l=initList()
    filterTypeValue(l,"in",100)
    assert l == [{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":28,"Value":66,"Type":"in","Description":"salary"}]
    l=initList()
    filterTypeValue(l,"out",100)
    assert l == [{"Day":13,"Value":70,"Type":"out","Description":"donuts"},{"Day": 25, "Value": 32, "Type": "out", "Description": "shoes"},
                 {"Day": 28, "Value": 74, "Type": "out", "Description": "hats"}]


def testUndo():
    l=initList()
    undoL=[[]]
    auxL = copy.deepcopy(l)
    undoL.append(auxL)
    removeType(l,"in")
    assert undoL == [[],[{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":2,"Value":140,"Type":"in","Description":"salary"},
       {"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
       {"Day":22,"Value":469,"Type":"in","Description":"salary"},{"Day":25,"Value":32,"Type":"out","Description":"shoes"},
       {"Day":25,"Value":180,"Type":"in","Description":"chocolate"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
       {"Day":28,"Value":74,"Type":"out","Description":"hats"},{"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]]
    l,undoL=undo(l,undoL)
    assert undoL == [[]] and l == [{"Day":2,"Value":60,"Type":"in","Description":"pizza"},{"Day":2,"Value":140,"Type":"in","Description":"salary"},
       {"Day":2,"Value":198,"Type":"out","Description":"clothes"},{"Day":13,"Value":70,"Type":"out","Description":"donuts"},
       {"Day":22,"Value":469,"Type":"in","Description":"salary"},{"Day":25,"Value":32,"Type":"out","Description":"shoes"},
       {"Day":25,"Value":180,"Type":"in","Description":"chocolate"},{"Day":28,"Value":66,"Type":"in","Description":"salary"},
       {"Day":28,"Value":74,"Type":"out","Description":"hats"},{"Day":30,"Value":190,"Type":"out","Description":"pancakes"}]

testRemoveInterval()
testAdd()
testInsert()
testRemoveDay()
testRemoveType()
testReplace()
testPrintList()
testListType()
testListValue()
testListBalance()
testSum()
testMax()
testFilterType()
testFilterTypeValue()
testUndo()
