def fct1(x, y):
    if x <= y:
        return True
    return False


def gnomeSort(lst, fct):
    c = 1
    length = len(lst)
    while c < length:
        cdt = fct(lst[c-1], lst[c])
        if cdt:
            c += 1
        else:
            aux = lst[c-1]
            lst[c-1] = lst[c]
            lst[c] = aux
            c -= 1
            if c == 0:
                c = 1


def fct2(x):
    if x < 100:
        return True
    return False


def filter(lst, fct, crt):
    newList = []
    for obj in lst:
        cdt = fct(obj, crt)
        if cdt:
            newList.append(obj)
    return newList

lst = [1, 3, 20, 4, 4, 15, 1]
gnomeSort(lst, fct1)
print(lst)
