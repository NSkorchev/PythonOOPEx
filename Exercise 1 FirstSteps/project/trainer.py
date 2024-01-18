from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):

        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # try:
        #     pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        # except StopIteration:
        # return "Pokemon is not caught"

        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        # return "Pokemon is not caught"

        for pokemon in self.pokemons:

            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            data += "- " + pokemon.pokemon_details() + "\n"

        return data


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
