import random
from math import ceil

class Individual:
    def __init__(self, items, max_weight):
        self.genotype = [False] * len(items)
        self.max_weight = max_weight
        self.weight_used = 0
        self.items = items
        self.score = 0

    def generate_genotype(self):
        for i in range(len(self.genotype)):
            self.genotype[i] = bool(random.getrandbits(1))
        self.correct_genotype()
        for i in range(len(self.items)):
            if self.genotype[i]:
                self.score += self.items[i].value

    def correct_genotype(self):
        counter = 0
        for i in range(len(self.items)):
            if self.genotype[i]:
                self.weight_used += self.items[i].weight
        while self.weight_used > self.max_weight:
            if self.genotype[counter]:
                self.genotype[counter] = False
                self.weight_used -= self.items[counter].weight
            counter += 1

    def breeding(self, ind_a, ind_b):
        for i in range(len(self.genotype)):
            if i< len(self.genotype)/2:
                self.genotype[i] = ind_a.genotype[i]
            else:
                self.genotype[i] = ind_b.genotype[i]
        self.correct_genotype()
        for i in range(len(self.items)):
            if self.genotype[i]:
                self.score += self.items[i].value
