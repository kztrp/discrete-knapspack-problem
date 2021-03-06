from item import Item
from genetic_algorithm import print_population, generate_population, run_algorithm, export_results
import random
from os import path, mkdir


def main():
    items = []
    random.seed(5345)
    number_of_items = int(input("Please enter number of items: "))
    for i in range(number_of_items):
        item = Item(random.randint(1, 10), random.randint(0, 75))
        items.append(item)
    print(items)
    weight = 0
    for i in range(number_of_items):
        weight += items[i].weight
    print(weight)
    max_weight = round(weight/2)
    population_size = int(input("Please enter population size: "))
    population = generate_population(population_size, max_weight, items)
    number_of_generations = int(input("Please enter number of generations: "))
    population = run_algorithm(population, number_of_generations)
    print_population(population)
    choice = input("Do you want to export results to textfile? (y/N) ")
    if choice == "y":
        parameters = {"Number of items": number_of_items, "Population size": population_size,
                      "Number of generations": number_of_generations}
        filename = input("Please enter filename: ")
        if not path.isdir("exported_results"):
            mkdir("exported_results")
        export_results(population, parameters, filename)


if __name__ == "__main__":
    main()

