import random

def level_1():
    global level
    level = 1

    global random1
    random1 = random.randint(0,9)

    global random2
    random2 = random.randint(0,9)

    
    
    

def level_2():
    global level
    level=2

    global random1
    random1= random.randint(10,50)

    global random2
    random2 = random.randint(10,50)
    

def level_3():
    global level
    level = 3

    global random1
    random1 = random.randint(51, 100)

    global random2
    random2 = random.randint(51, 100)

def addition():
    global operation
    operation = '+'

def subtraction():
    global operation
    operation = '-'

def multiplication():
    global operation
    operation = '*'

def division():
    global operation
    operation = '/'

