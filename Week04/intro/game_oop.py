## OOP implementation of turn-based game
import random

# create a blueprint of an object
class Stats:
    def __init__(self, attack=0, defense=0):
        # set up the attributes
        self.attack = attack
        self.defense = defense

    def add_stats(self, other):
        # this function receives two Stats objects
        # need to create a NEW Stats containing the combi of both stats attributes
        return Stats(self.attack + other.attack, self.defense + other.defense)

    @property
    def power(self): # whenever you @property, make sure the func only has 1 arg
        # the purpose of this is to report a combi of attributes
        # and not to DO something (unlike regular methods)
        return self.attack + self.defense # power is a computed PROPERTY


    @property
    def dbl_stats(self):
        # this is a weird property function although it will technically run
        # property is usually used to report a value in a clean manner/compute a value on the fly
        # not to APPLY something to the instance
        self.attack = self.attack * 2
        self.defense = self.defense * 2
        return self.attack + self.defense

stat_one = Stats(10, 20) # instantiating a Stats object with 10 attack and 20 defense
stat_two = Stats(20, 30) # another instance of Stats object with 20 attack and 30 defense
stat_three = stat_one.add_stats(stat_two) # calling a method in the Stats class
print(stat_two.power)

# Weapon: a user defined object that a Character will be COMPOSED of (has a).
# Weapon itself is composed of a Stats object (its bonus), so composition
# can nest, just like RobotTurtle has a Coordinate in the notes.
# ---------------------------------------------------------------------------
class Weapon:
    def __init__(self, name, min_damage, max_damage, bonus=None):
        self.name = name                      # uses the property setter below
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._bonus = bonus or Stats(0, 0)    # COMPOSITION: weapon has a Stats

    # STORED PROPERTY with validation in the setter (same pattern as the notes).
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value != "":
            self._name = value

    # Read only property (getter only), like pos in the notes.
    @property
    def bonus(self):
        return self._bonus

    # METHOD (a verb, an action). It also shows why this cannot be a computed
    # property: it performs a random roll, i.e. it is an action, not an
    # intrinsic noun like power.
    def roll_damage(self):
        return random.randint(self._min_damage, self._max_damage)

    def __str__(self):
        return f"{self.name} ({self._min_damage}-{self._max_damage}, +{self._bonus})"


# ---------------------------------------------------------------------------
# Character: composed of a Weapon and a base Stats. Demonstrates stored
# properties with validation, a computed property, and the method vs
# computed property distinction.
# ---------------------------------------------------------------------------
class Character:
    def __init__(self, name, max_hp, base_stats, weapon):
        # ENCAPSULATION: single leading underscore says "internal, use the property".
        self._max_hp = max_hp
        self.name = name            # goes through the name setter (validation)
        self.hp = max_hp            # goes through the hp setter (clamping)
        self._base_stats = base_stats   # COMPOSITION: character has a Stats
        self._weapon = weapon            # COMPOSITION: character has a Weapon

    # --- STORED PROPERTY: name, validated ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value != "":
            self._name = value

    # --- STORED PROPERTY: hp, clamped between 0 and max_hp ---
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if isinstance(value, int):
            # all writes pass through here, so we clamp ONCE, in ONE place
            self._hp = max(0, min(value, self._max_hp))

    # --- read only property ---
    @property
    def max_hp(self):
        return self._max_hp

    @property
    def weapon(self):
        return self._weapon

    # --- COMPUTED PROPERTY: derived from an attribute, no setter, cheap, a noun ---
    @property
    def is_alive(self):
        return self._hp > 0

    # --- COMPUTED PROPERTY that uses operator overloading (__add__) ---
    # total_stats = base stats combined with the weapon's bonus.
    @property
    def total_stats(self):
        return self._base_stats + self._weapon.bonus

    # --- METHOD (takes an argument, performs an action) ---
    def take_damage(self, amount):
        self.hp = self._hp - amount   # setter clamps, so hp never goes below 0

    # --- METHOD that takes ANOTHER OBJECT as an argument ---
    # This must be a method, not a computed property: it needs an argument
    # (the target) and it changes the world. Computed properties take only self.
    def attack(self, target):
        raw = self._weapon.roll_damage() + self.total_stats.attack
        dealt = max(1, raw - target.total_stats.defense)  # defense mitigates
        target.take_damage(dealt)
        print(f"  {self.name} attacks {target.name} for {dealt}.")

    # --- SPECIAL METHOD ---
    def __str__(self):
        return f"{self.name}: {self._hp}/{self._max_hp} HP [{self.total_stats}], using {self._weapon.name}"


# ---------------------------------------------------------------------------
# A simple turn based loop. No inheritance needed: both fighters are just
# Character objects, so we call the same attack() method on each.
# ---------------------------------------------------------------------------
def battle(a, b):
    round_no = 1
    while a.is_alive and b.is_alive:
        print(f"Round {round_no}")
        a.attack(b)
        if b.is_alive:
            b.attack(a)
        print(" ", a)
        print(" ", b)
        print("-" * 50)
        round_no += 1

    winner = a if a.is_alive else b
    print(f"{winner.name} wins!")


if __name__ == "__main__":
    random.seed(2)  # repeatable demo for class

    # Composition in action: each weapon carries a Stats bonus,
    # each character carries base Stats plus a Weapon.
    sword = Weapon("Iron Sword", 4, 8, bonus=Stats(attack=2, defense=1))
    claws = Weapon("Claws", 3, 6, bonus=Stats(attack=1, defense=0))

    knight = Character("Knight", max_hp=40, base_stats=Stats(3, 4), weapon=sword)
    beast = Character("Beast", max_hp=34, base_stats=Stats(4, 1), weapon=claws)

    # __str__ in action
    print(knight)
    print(beast)

    # operator overloading in action: combine two Stats with +
    combined = knight.total_stats + beast.total_stats
    print("Combined stats (Stats __add__):", combined, "-> power", combined.power)
    print("-" * 50)

    battle(knight, beast)
