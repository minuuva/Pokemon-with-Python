from typing import List, Tuple

class Pokemon:
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int]]) -> None:
        
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

class FightingPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int]]) -> None:
        
        #Fighting-type Pokemons receive a 20% increase in attack points
        attack_points = int(attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Fighting"

    def display_type(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class AquaPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int]]) -> None:
        
        special_attack_points = int(special_attack_points * 1.1)
        defense_points = int(defense_points * 1.1)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Aqua"
    
    def display_tyoe(self):
        print(f"{self.name} is a {self.type}-type Pokémon.")

class ElectricPokemon(Pokemon):
    def __init__(self, name: str, pokedexid: str, level: int, hp: int, attack_points: int, defense_points: int, 
                 special_attack_points: int, special_defense_points: int, speed: int, experience_points: int,
                 skill: List[Tuple[str, int]]) -> None:
        
        special_attack_points = int(special_attack_points * 1.2)
        
        super().__init__(name, pokedexid, level, hp, attack_points, defense_points, 
                         special_attack_points, special_defense_points, speed, experience_points, skill)
        self.type = "Electric"
        
        

machop = FightingPokemon('Machop', '040', 1, 70, 80, 50, 35, 35, 35, 0, [('Revenge', 60), ('Low Sweep', 60)])
piplup = AquaPokemon('piplup', '007', 1, 53, 51, 53, 61, 56, 40, 0, [('water_gun', 40), ('peck', 35)])
shinx = ElectricPokemon('shinx', '017', 1, 45, 65, 34, 40, 34, 45, 0, [('thunder_shock', 40), ('bite', 60)])




#print(f"Pokemon Name: {machop.name}, Type: {machop.type}, HP: {machop.hp}, Attack Points: {machop.attack_points}, Skills: {machop.skill}")