class Weapon:
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        self.name = name
        self.weight = weight
        self.base_damage = base_damage
        self.rarity_mod = rarity_mod
 # 'scaling' is a dictionary {"strength": 1.5, "dexterity": 0.5}
        self.scaling = scaling
# zone is an action list
        self.zone = zone
    def calculate_damage(self, character):
        scaling_damage = 0
        for attribute, factor in self.scaling.items():
            attribute_value = getattr(character, attribute, 0)
            scaling_damage += attribute_value * factor
        total_damage = (self.base_damage + scaling_damage) * self.rarity_mod
        return total_damage
## MAIN WEAPON CLASSES
class MeleeWeapon(Weapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)
class RangedWeapon(Weapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

## 1ST LEVEL SUBCLASSES
class OneHandedMelee(MeleeWeapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)
class TwoHandedMelee(MeleeWeapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

## 2ND LEVEL SUBCLASSES
class Dagger(OneHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)
    def get_base_damage(self):
        return self.base_damage
    def get_rarity(self):
        return self.rarity_mod

class ShortSword(OneHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class Sword(OneHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class Axe(OneHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class MediumSword(OneHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class LongSword(TwoHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class BattleAxe(TwoHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class WarHammer(TwoHandedMelee):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class ShortBow(RangedWeapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class LongBow(RangedWeapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)

class CrossBow(RangedWeapon):
    def __init__(self, name, weight, base_damage, rarity_mod, scaling, zone):
        super().__init__(name, weight, base_damage, rarity_mod, scaling, zone)
##weapon creation
bronze_dagger = Dagger(name="Bronze Dagger", weight=2, base_damage=8, rarity_mod=1.0, scaling={"dexterity": 1.0}, zone=None)
bronze_straight_sword = MediumSword(name="Bronze Straight Sword", weight=4, base_damage=12, rarity_mod=1.0, scaling={"dexterity": 0.4, "strength": 0.6}, zone=None)
zone_test = Dagger(name="Zone", weight=2, base_damage=10, rarity_mod=1.0, scaling={"dexterity": 1.0}, zone=dagger_zone)
print(f"Dagger {bronze_dagger.name}'s damage: {bronze_dagger.get_base_damage()} rarity: {bronze_dagger.get_rarity()}")