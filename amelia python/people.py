import random
dances = ["Foxtrot!","Waltz!","Tango!","Charleston!","Twist!"]
class Person:
    def breathe(self):
        print("breathing")
    def walk(self):
        print("walking")
    def eat(self,foo):
        print("eating %s." % foo)
class Man(Person):
    pass
class Woman(Person):
    def dance(self):
        print(random.choice(dances))
class Boy(Man):
    pass
class Adult_Man(Man):
    def flirt(self):
        print("Hi, pretty")
class Girl(Woman):
    pass
class Adult_Woman(Woman):
    pass
