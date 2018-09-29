print('---------------Inheritance-----------------')
class Animal():
    def __init__(self):
        print('Hi,I am the super class animal')
    def whatami(self):
        print('Mightiest of all')
    def q(self):
        print('hello')
class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print('Hi,I am dog')
d=Dog()
d.whatami()
d.q()
print('----------------Special methods------------------')
class Book():
    def __init__(self,name,author,publication):
        self.name=name
        self.author=author
        self.publication=publication
    def __str__(self):
        return "Name: {}, Author: {}, Publication: {}".format(self.name,self.author,self.publication)
b=Book('Python','John','Pearson')
print(b)
