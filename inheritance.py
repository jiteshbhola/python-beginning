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
