import random

def make_stats(attack, defense):
    return {"attack": attack, "defense": defense}

def stats_power(s):
    return s["attack"] + s["defense"]

def add_stats(a,b):
    return make_stats(a["attack"] + b["attack"], a["defense"] + b["defense"])

def stats_str(s):
    return f"ATK {s['attack']} \ DEF {s['defense']}"

def make_weapon(name, min_damage, max_damage, bonus=None):
    return {
            "name": name,
            "min_damage": min_damage,
            "max_damage": max_damage,
            "bonus": bonus if bonus is not None else make_stats(0,0),
            }

def roll_damage(weapon):
    return random.randint(weapon["min_damage"], weapon["max_damage"])

def make_character(name, max_hp, base_stats, weapon):
    return {
            "name": name,
            "max_hp": max_hp,
            "hp": max_hp,
            "base_stats": base_stats,
            "weapon": weapon,
            }


def is_alive(c):             # would be a COMPUTED PROPERTY (c.is_alive)
    return c["hp"] > 0


def total_stats(c):          # would be a COMPUTED PROPERTY that uses +
    return add_stats(c["base_stats"], c["weapon"]["bonus"])


def take_damage(c, amount):
    c["hp"] = c["hp"] - amount
    # We must clamp here by hand. If we forget in any one place, hp breaks.
    if c["hp"] < 0:
        c["hp"] = 0
    if c["hp"] > c["max_hp"]:
        c["hp"] = c["max_hp"]

def character_str(c):        # would be __str__
    return (f"{c['name']}: {c['hp']}/{c['max_hp']} HP "
            f"[{stats_str(total_stats(c))}], using {c['weapon']['name']}")


def attack(attacker, target):
    raw = roll_damage(attacker["weapon"]) + total_stats(attacker)["attack"]
    dealt = max(1, raw - total_stats(target)["defense"])  # defense mitigates
    take_damage(target, dealt)
    print(f"  {attacker['name']} attacks {target['name']} for {dealt}.")


def battle(a, b):
    round_no = 1
    while is_alive(a) and is_alive(b):
        print(f"Round {round_no}")
        attack(a, b)
        if is_alive(b):
            attack(b, a)
        print(" ", character_str(a))
        print(" ", character_str(b))
        print("-" * 50)
        round_no += 1

    winner = a if is_alive(a) else b
    print(f"{winner['name']} wins!")


if __name__ == "__main__":
    random.seed(2)  # same seed as game_week4.py, so the fight is identical

    sword = make_weapon("Iron Sword", 4, 8, make_stats(2, 1))
    claws = make_weapon("Claws", 3, 6, make_stats(1, 0))

    knight = make_character("Knight", 40, make_stats(3, 4), sword)
    beast = make_character("Beast", 34, make_stats(4, 1), claws)

    print(character_str(knight))
    print(character_str(beast))

    # No operator overloading, so combining stat blocks is a manual call.
    combined = add_stats(total_stats(knight), total_stats(beast))
    print("Combined stats (manual add_stats):", stats_str(combined),
          "-> power", stats_power(combined))
    print("-" * 50)

    battle(knight, beast)
