import unittest
from genetic_algorithm import roulette_breeding, generate_population, export_results
from os import rmdir, path, mkdir, remove
from individual import Individual
import random
from item import Item


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.items = []
        for i in range(5):
            item = Item(random.randint(1, 10), random.randint(0, 75))
            self.items.append(item)
        weight = 0
        for i in range(5):
            weight += self.items[i].weight
        print(weight)
        max_weight = round(weight / 2)
        self.population = generate_population(10, max_weight, self.items)

    def test_breeding(self):
        new_pop = roulette_breeding(self.population, 10)
        for i in range(len(new_pop)):
            self.assertLessEqual(new_pop[i].weight_used, new_pop[i].max_weight)

    def test_export(self):
        if not path.isdir("exported_results"):
            mkdir("exported_results")
        self.assertTrue(export_results(self.population, "", "Test_results.txt"))
        remove("exported_results/Test_results.txt")
        rmdir("exported_results")

if __name__ == '__main__':
    unittest.main()
