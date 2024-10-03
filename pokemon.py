import random
from typing import List, Tuple

class Pokemon:
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]]) -> None:
        
        self.name = name
        self.pokedexid = pokedexid
        self.level = level
        self.hp = hp
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.special_attack_points = special_attack_points
        self.special_defense_points = special_defense_points
        self.speed = speed
        self.experience_points = experience_points
        self.skill = skill
        self.fight_status: bool = False
        self.alive: bool = True

    def train(self):
        experience_gain = random.randint(5, 13)
        self.experience_points += experience_gain
        print(f"{self.name} gained {experience_gain} experience points!")
        
        if self.experience_points >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience_points = 0
        print(f"{self.name}'s body seems to be growing!")
        print(f"{self.name} has leveled up to level {self.level}!")
        

class FightingPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]]) -> None:
        
        # Fighting-type Pokemons receive a 20% increase in attack points
        attack_points = int(attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Fighting"

    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class AquaPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]]) -> None:
        
        special_attack_points = int(special_attack_points * 1.1)
        defense_points = int(defense_points * 1.1)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Aqua"
    
    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class ElectricPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]]) -> None:
        
        special_attack_points = int(special_attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Electric"

    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class GrassPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]]) -> None:
        
        special_defense_points = int(special_defense_points * 1.3)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Grass" 
    
    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")


machop = FightingPokemon('Machop', '040', 1, 70, 80, 50, 35, 35, 35, 0, [('revenge', 60, 'regular'), ('low Sweep', 60, 'regular')])
piplup = AquaPokemon('Piplup', '007', 1, 53, 51, 53, 61, 56, 40, 0, [('water gun', 40, 'special'), ('peck', 35, 'special')])
shinx = ElectricPokemon('Shinx', '017', 1, 45, 65, 34, 40, 34, 45, 0, [('thunder shock', 40, 'special'), ('bite', 60, 'regular')])
turtwig = GrassPokemon('Turtwig', '001', 1, 55, 68, 64, 45, 55, 31, 0, [('absorb', 20, 'special'), ('razor leaf', 55, 'special')])


def battle(pokemon1: Pokemon, pokemon2: Pokemon):
    print(f"A battle begins between {pokemon1.name} and {pokemon2.name}!")
    
    if pokemon1.speed > pokemon2.speed:
        first = pokemon1
        second = pokemon2
    elif pokemon2.speed > pokemon1.speed:
        first = pokemon2
        second = pokemon1
    else:
        first, second = random.sample([pokemon1, pokemon2], 2)
    print(f"{first.name} attacks first!")
    
    while first.hp > 0 and second.hp > 0:
        # first pokemon attack
        move = random.choice(first.skill)
        if move[2] == 'regular':
            damage = max(first.attack_points - second.defense_points, 0)
            print(f"{first.name} used {move[0]} and dealt {damage} damage to {second.name}!")
        else:
            damage = max(first.special_attack_points - second.special_defense_points, 0)
            print(f"{first.name} used {move[0]} and dealt {damage} damage to {second.name}!")

        second.hp -= damage
        
        if second.hp <= 0:
            print(f"{second.name} fainted! {first.name} wins!")
            
        
        # second pokemon attack
        move = random.choice(second.skill)
        if move[2] == 'regular':
            damage = max(second.attack_points - first.defense_points, 0)
            print(f"{second.name} used {move[0]} and dealt {damage} damage to {first.name}!")
            
        else:
            damage = max(second.special_attack_points - first.special_defense_points, 0)
            print(f"{second.name} used {move[0]} and dealt {damage} damage to {first.name}!")
            
        first.hp -= damage
        if first.hp <= 0:
            print(f"{first.name} fainted! {second.name} wins!")
            return
        
battle(machop, shinx)