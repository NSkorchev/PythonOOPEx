from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Spiderman", 20, 100.0, 10.0)
        self.enemy = Hero("Goblin", 5, 150.0, 15.0)

    def test_correct_initialization(self):
        self.assertEqual("Spiderman", self.hero.username)
        self.assertEqual(20, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_battle_enemy_hero_name_same_as_hero_raise_ex(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_with_zero_energy_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_hero_with_zero_hero_energy_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_enemy_remove_health_after_draw(self):
        self.hero.health = 75

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_enemy_and_win_expect_hero_stats_improve(self):

        result = self.hero.battle(self.enemy)

        self.assertEqual(21, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_enemy_and_loose_expect_enemy_stats_improve(self):
        self.enemy.health = 250
        self.hero.health = 75

        result = self.hero.battle(self.enemy)

        self.assertEqual(6, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(20, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_correct__str__(self):
        self.assertEqual(
            f"Hero Spiderman: 20 lvl\n"
            f"Health: 100.0\n"
            f"Damage: 10.0\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()
