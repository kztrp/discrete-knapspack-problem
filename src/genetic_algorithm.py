from individual import Individual
from math import ceil, floor
import random


def print_population(population):
    for individual in population:
        print(individual)


def generate_population(size, max_weight, items):
    population = []
    for i in range(size):
        individual = Individual(items, max_weight)
        individual.generate_genotype()
        population.append(individual)
    return population


def roulette_breeding(population, iteration):
    total_score = 0
    copied_size = floor(0.15 * len(population))
    bred_size = ceil(0.85 * len(population))
    if bred_size % 2 == 1:
        copied_size += 1
        bred_size -= 1
    population.sort(key=lambda x: x.score, reverse=True)
    new_population = []
    for i in range(copied_size):
        new_population.append(population[i])
    for individual in population:
        total_score += individual.score
    for i in range(round(bred_size/2)):
        found = [False, False]
        selected_value = [random.randint(0, total_score), random.randint(0, total_score)]
        parents = []
        for individual in population:
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
        ind_a.iteration = iteration
        ind_b.iteration = iteration
        new_population.append(ind_a)
        new_population.append(ind_b)

    new_population.sort(key=lambda x: x.score, reverse=True)
    return new_population


def run_algorithm(population, iterations):
    new_population = population
    for i in range(iterations):
        new_population = roulette_breeding(new_population, i)
    return new_population


def export_results(population, parameters, filename):
    try:
        with open("exported_results/"+filename, 'w+') as f:
            if parameters != "":
                for x, y in parameters.items():
                    f.write("{}: {}\n".format(x, y))
            f.write("\n\n")
            for individual in population:
                f.write(individual.__repr__())
        return True
    except NotADirectoryError and FileNotFoundError:
        return False
