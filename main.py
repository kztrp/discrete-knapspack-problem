from individual import Individual
from item import Item
import random

def main():
    items = []
    random.seed(5345)
    for i in range(8):
        item = Item(random.randint(1, 10), random.randint(0, 75))
        items.append(item)
    print(items)
    weight = 0
    for i in range(len(items)):
        weight += items[i].weight
    print(weight)
    max_weight = round(weight/2)
    ind1 = Individual(items, max_weight)
    ind1.generate_genotype()
    ind2 = Individual(items, max_weight)
    ind2.generate_genotype()
    print(ind1.genotype)
    print(ind2.genotype)
    ind3 = Individual(items, max_weight)
    ind3.breeding(ind1, ind2)
    print(ind3.genotype)
    ind4 = Individual(items, max_weight)
    ind4.breeding(ind2, ind1)
    print(ind4.genotype)
    print('\n')
    print("{}/{}".format(ind1.weight_used, max_weight))
    print("{}/{}".format(ind2.weight_used, max_weight))
    print("{}/{}".format(ind3.weight_used, max_weight))
    print("{}/{}".format(ind4.weight_used, max_weight))


if __name__ == "__main__":
    main()