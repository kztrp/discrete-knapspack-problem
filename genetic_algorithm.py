from individual import Individual
from math import ceil, floor
import random


def print_population(population, max_weight):
    for individual in population:
        print(individual.genotype)
        print("{}/{}".format(individual.weight_used, max_weight))
        print("Score: {}\n".format(individual.score))

def generate_population(size, max_weight, items):
    population = []
    for i in range(size):
        individual = Individual(items, max_weight)
        individual.generate_genotype()
        population.append(individual)
    return population


def roulette_breeding(population):
    total_score = 0
    copied_size = floor(0.3 * len(population))
    bred_size = ceil(0.7 * len(population))
    if bred_size % 2 == 1:
        copied_size += 1
        bred_size -= 1
    population.sort(key=lambda x: x.score, reverse=True)
    new_population = [population[:copied_size]]
    for individual in population:
        total_score += individual.score
    for i in range(bred_size/2):
        found = [False, False]
        selected_value = [random.randint(0, total_score), random.randint(0, total_score)]
        for individual in population:
            parents = []
            selected_value[0] -= individual.score
            selected_value[1] -= individual.score
            if not found[0] and selected_value[0] <= 0:
                parents.append(individual)
            if not found[1] and selected_value[1] <= 0:
                parents.append(individual)
            if found[0] and found[1]:
                break
        ind_a = Individual(parents[0].items, parents[0].max_weight)
        ind_b = Individual(parents[0].items, parents[0].max_weight)
        ind_a.breeding(parents[0], parents[1])
        ind_b.breeding(parents[1], parents[0])
        new_population.append(ind_a, ind_b)
    return new_population


