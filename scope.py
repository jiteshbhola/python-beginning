print('--------------------Scope of python vairables-----------------')
x=25  #global-declaration
def fu():
    x=22  #local-declaration-limited to the scope of function
    return x
print(x)  #calls global x
print(fu())    #calls fu #
def f():
    x='hahahahahahahaahaa'
    print('hello '+ x)
f()
print(x)
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
print(x)
print(printer())
print(x)
