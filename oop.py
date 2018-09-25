# print("---------------Class with attribute and a special function--------------------")
# class Jitesh():
#     pass
# a=Jitesh()
# print(type(a))
# class Cat():
#     legs=4 #class object attribute,true for all values
#     def __init__(self,color,eyes,tail,name):
#         self.eyes=eyes
#         self.tail=tail
#         self.color=color
#         self.name=name
# mycat=Cat('black','grey','long','billi')  #follows order as specified in init
# mycat=Cat(tail='long',color='grey',eyes='black',name='billi') #follows attrib value as assigned,can be random
#
# print(mycat.color)
# print(mycat.eyes)
# print(mycat.tail)
# print(mycat.name)
# print(mycat.legs)
print("---------------Class with attribute and functions--------------------")
class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
         return self.radius*self.radius*Circle.pi
    def setradius(self,newradii):
        self.radius=newradii
myc=Circle(3)
myc.setradius(10)
# myc.radius=10  #redefine attrib value
print(myc.radius)
print(myc.area())
