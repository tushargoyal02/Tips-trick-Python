#pythontutor.com


# code in global scope can't use any local variables
def sp():
    egg=99

sp()
#print(egg)



# code in one local scope can't be use as local  scope of other
def spam1():
    eggs=11
    bacon()
    print(eggs)

def bacon():
    ga=11
    eggs=1
spam1()

def hello()
    ab=123
    print(ab)



#global varibale can be read by local scope


#changing the global value

def spanm():
    global eggs
    eggs='hello'
    print(eggs)

eggs=42
spanm()
print(eggs)
