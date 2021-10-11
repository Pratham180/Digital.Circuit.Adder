def and_gate(a, b): #defining function for and gate
    if a == 0 and b == 0:  #if else loop
        return 0
    elif a == 1 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 0
    else:
        return 1


def or_gate(a, b): #defining function for or gate
    if a == 0 and b == 0:  # if else loop
        return 0
    elif a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    else:
        return 1


def not_gate(a): #definig function for not gate
    if a == 0: #if else loop
        return 1
    else:
        return 0


def xor_gate(a, b): #defining function xor gate
    if a == 0 and b == 0: #if else loop
        return 0
    elif a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    else:
        return 0


def nand_gate(a, b): #defining function nand gate
    if a == 0 and b == 0: #if else loop
        return 1
    elif a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    else:
        return 0


def nor_gate(a, b):  #defining function nor gate
    if a == 0 and b == 0: # if else loop
        return 1
    elif a == 1 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 0
    else:
        return 0


def x_nor_gate(a, b): #defining function xnor gate 
    if a == 0 and b == 0: #if else loop
        return 1
    elif a == 1 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 0
    else:
        return 1
