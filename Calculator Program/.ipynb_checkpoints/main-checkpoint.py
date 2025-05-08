def addmultiplenumbers(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum

def multiplymultiplenumbers(list):
    mul=1
    for i in list:
        mul=mul*i
    return mul

def isiteven(num):
    if num%2==0:
        return True
    else:
        return False

def isitaninteger(num):
    if num==int(num):
        return True
    else:
        return False

