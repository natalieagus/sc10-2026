class Human:
    def __init__(self, name):
        self._name = name
        self.hometown = "City A"

    @property
    def name(self):
        return self._name

    def attack(self):
        print ("[Human, attack]: attack")

    def heal(self):
        print("[Human, heal]: heal")

h= Human("Alpha")
# usually don't do this
# it would work, but it's not recommended to set attributes directly in practice
# if you need to set hometown outside of the Class, then you should make hometown a property, and store a private attr _hometown internally
h.hometown = "City B"

# Python allows you to assign a whole new attribute outside of the class
# since .money isn't defined in the init, then a new one here is created for you during runtime
# its as if now your human grows money suddenly (has a new attr money)
# although this works, please don't do this
# declare ALL attributes you need during __init__ and never suddenly create one during runtime
# use PROPERTY if you need to set any attr value outside of the Class
# this is dangerous if you have typo, e.g: set h.hmetown ---> new attribute created
h.money = "2000"
print(h.money)

class Wizard(Human):
    def cast_spell(self):
        print("Wizard casts spell")

class Archer(Human):
    def __init__(self, agi_stats, name):
        self._agi_stats = agi_stats

class Warrior(Human): # my super class is Human
    def __init__(self, str_stats, name):
        self._str_stats = str_stats
        # also call the parent's __init__ function
        # METHOD 1: Human.__init__(self, name) # call it by the direct class name OR
        # METHOD 2: super().__init__(name) # or via super() reference, self is automatically passed
        super().__init__(name) # super() means reference to my superclass

    def attack(self):
        print ("[Warrior, attack]: attack")

    def heal(self):
        super().heal()
        print("[Warrior, heal]: heal")

class Knight(Warrior):
    def __init__(self, def_stats, str_stats, name):
        self._def_stats = def_stats
        super().__init__(str_stats, name)

    # method override, totally not calling the parent's one
    def attack(self):
        print ("[Knight, attack]: attack")

    # method override but still also call the parent's one
    def heal(self):
        super().heal()
        print("[Knight, heal]: heal")

k = Knight(30, 60, "Ethan")
print(k.name)
k.attack() # this will print Knight's attack because Python will find the youngest function, which is Knight's attack
# if Knight doesn't have an attack() method, then it will go up 1 level (Warrior), and try to find that method
k.heal() # because we call super() first, the printout from the oldest class appear first

w = Warrior(80, "David")
print(w.name) # this works now because we explicitly call super().__init__ which refers to Human's __init__

a = Archer(50, "Charles")
print(a.name) # this results in error because Archer already has an __init__ function, so Python is calling that instead of Human's __init__ function
# order of function discovery: start from this class, if not found, go one level up (and repeat)
# a.name is not highlighted as red because Python can find the property name
# the issue is that the init func of Human is NOT called, so self._name is not set, and calling prop a.name will access self._name >> no attribute _name because it's never set

# init func in Human is inherited by Wizard
# although there's no init func in Wizard, it expects the name param, which is the __init__ func of Human
w = Wizard("Alice")
w.name # property inherited from Human
w.cast_spell() # method in Wizard
print(isinstance(w, Wizard)) # True
print(isinstance(w, Human)) # Also True
# Wizard is an instance of both Wizard and Human


h = Human("Bob")
# h.cast_spell() # Bob is not a Wizard
print(isinstance(h, Human)) # False
