from typing import Dict


class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild: str = Player.DEFAULT_GUILD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = '\n'.join([f"==={skill} - {mp}" for skill, mp in self.skills.items()])

        return f"Name: {self.name}\n" + \
               f"Guild: {self.guild}\n" + \
               f"HP: {self.hp}\n" + \
               f"MP: {self.mp}\n" + \
               f"{skills}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
