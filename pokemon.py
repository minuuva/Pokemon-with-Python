import random
from typing import List, Tuple

class Pokemon:
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]], second_name: str, evolution_level: int) -> None:
        
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
        self.second_name = second_name
        self.evolution_level = evolution_level
        self.evolved = False

    def train(self):
        experience_gain = random.randint(5, 13)
        self.experience_points += experience_gain
        print(f"{self.name} gained {experience_gain} experience points!")
        
        if self.experience_points >= 100:
            self.level_up()
    
    def level_up(self):
        if self.experience_points >= 200:
            self.level += 1
            self.experience_points = 0
            print(f"{self.name}'s body seems to be growing!")
            print(f"{self.name} leveled up to level {self.level}!")
        
        if self.level >= self.evolution_level and not self.evolved:
            self.evolve()
               
    def evolve(self):
        if not self.evolved: # true initially, beacuse self.evolved in False
            print(f"{self.name} is evolving!")
            self.name = self.second_name
            self.hp = int(self.hp * 1.3)
            self.attack_points = int(self.attack_points * 1.3)
            self.defense_points = int(self.defense_points * 1.3)
            self.special_attack_points = int(self.special_attack_points * 1.3)
            self.special_defense_points = int(self.special_defense_points * 1.3)
            self.speed = int(self.speed * 1.3)
            self.evolved = True # to ensure that the Pokemon doesn't evolve again
            print(f"{self.name} has evolved!")     

class FightingPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]], second_name: str, evolution_level: int) -> None:
        
        # Fighting-type Pokemons receive a 20% increase in attack points
        attack_points = int(attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill, second_name, evolution_level)
        self.type = "Fighting"

    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class AquaPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]], second_name: str, evolution_level: int) -> None:
        
        special_attack_points = int(special_attack_points * 1.1)
        defense_points = int(defense_points * 1.1)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill, second_name, evolution_level)
        self.type = "Aqua"
    
    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class ElectricPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]], second_name: str, evolution_level: int) -> None:
        
        special_attack_points = int(special_attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill, second_name, evolution_level)
        self.type = "Electric"

    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class GrassPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int, str]], second_name: str, evolution_level: int) -> None:
        
        special_defense_points = int(special_defense_points * 1.3)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill, second_name, evolution_level)
        self.type = "Grass" 
    
    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")


machop = FightingPokemon('Machop', '040', 1, 100, 80, 50, 35, 35, 35, 0, [('revenge', 30, 'regular'), ('low Sweep', 30, 'regular'), ('vital throw', 20, 'special')], 'Machoke', 16)
piplup = AquaPokemon('Piplup', '007', 1, 100, 51, 53, 61, 56, 40, 0, [('water gun', 40, 'special'), ('peck', 35, 'special'), ('fury attack', 30, 'regular')], 'Prinplup', 18)
shinx = ElectricPokemon('Shinx', '017', 1, 100, 65, 34, 40, 34, 45, 0, [('thunder shock', 40, 'special'), ('bite', 40, 'regular'), ('spark', 40, 'regular')], 'Luxio', 17)
turtwig = GrassPokemon('Turtwig', '001', 1, 100, 68, 64, 45, 55, 31, 0, [('absorb', 20, 'special'), ('razor leaf', 45, 'special'), ('bite', 40, 'regular')], 'Grotle', 16)

pokemon_list = [machop, piplup, shinx, turtwig]

#for i in pokemon_list:
    #print(i.defense_points)

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
            # for now, damage is calculated as the move's damage 
            damage = move[1]
            print(f"{first.name} used {move[0]} and dealt {damage} damage to {second.name}!")
        else:
            damage = move[1]
            print(f"{first.name} used {move[0]} and dealt {damage} damage to {second.name}!")

        second.hp -= damage
        
        if second.hp <= 0:
            print(f"{second.name} fainted! {first.name} wins!")
            return
            
        
        # second pokemon attack
        move = random.choice(second.skill)
        if move[2] == 'regular':
            damage = move[1]
            print(f"{second.name} used {move[0]} and dealt {damage} damage to {first.name}!")
            
        else:
            damage = move[1]
            print(f"{second.name} used {move[0]} and dealt {damage} damage to {first.name}!")
            
        first.hp -= damage
        if first.hp <= 0:
            print(f"{first.name} fainted! {second.name} wins!")
            return
        

while machop.level < 16:
    machop.train()