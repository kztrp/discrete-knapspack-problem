from unittest import TestCase
from individual import Individual
from item import Item
import random


class TestIndividual(TestCase):
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
        self.ind = Individual(self.items, max_weight)

    def test_generate_genotype(self):
        self.ind.generate_genotype()
        self.assertEqual(len(self.ind.genotype), len(self.items))

    def test_correct_genotype(self):
        self.ind.generate_genotype()
        self.ind.correct_genotype()
        self.assertLessEqual(self.ind.weight_used, self.ind.max_weight)

    def test_breeding(self):
        ind2 = Individual(self.items, self.ind.max_weight)
        ind3 = ind2
        self.ind.generate_genotype()
        ind2.generate_genotype()
        self.ind.correct_genotype()
        ind2.correct_genotype()
        ind3.breeding(self.ind, ind2)
        self.assertLessEqual(ind3.weight_used, ind3.max_weight)
