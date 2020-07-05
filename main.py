from item import Item
from genetic_algorithm import print_population, generate_population, run_algorithm
import random


def main():
    items = []
    random.seed(5345)
    for i in range(128):
        item = Item(random.randint(1, 10), random.randint(0, 75))
        items.append(item)
    print(items)
    weight = 0
    for i in range(len(items)):
        weight += items[i].weight
    print(weight)
    max_weight = round(weight/2)
    population = generate_population(100, max_weight, items)
    population=run_algorithm(population, 20)
    print_population(population, max_weight)


if __name__ == "__main__":
    main()

