from numpy import floor
import roosterfitness
import roostergen
from random import randint


# population = []
# population_size = 1000
# dagen = 5
# daguuren = 6
# vakken = [
#     [0, 0, '-           '],
#     [1, 4, 'Informatica '],
#     [2, 3, 'Wiskunde    '],
#     [3, 3, 'Engels      '],
#     [4, 5, 'Nederlands  '],
#     [5, 2, 'Natuurkunde '],
#     [6, 4, 'Scheikunde  '],
#     [7, 3, 'Duits       ']
# ]


def gen_first_population(population_size: int, vakken: list, dagen: int, daguuren: int):
    population = []
    fault = []
    i = population_size
    while i > 0:
        rooster = roostergen.gen_rooster(vakken, dagen, daguuren)
        fitness, tempfault = roosterfitness.calc_fitness(rooster, vakken)
        for j in range(len(tempfault)):
            fault.append(tempfault[j])
        rooster_fitness = [fitness, rooster, fault]
        fault = []
        population.append(rooster_fitness)
        i -= 1
    return population


def get_top_populations(population: list, ammount: int):
    sortedpopulation = sorted(population, reverse=True)
    toppopulation = []
    for i in range(ammount):
        toppopulation.append(sortedpopulation[i])
    return toppopulation


def mutate(rooster: list, rate: int):
    opties = roostergen.roosteropties(rooster)
    for _ in range(rate):
        pos1 = opties.pop(randint(0, len(opties) - 1))
        pos2 = opties.pop(randint(0, len(opties) - 1))
        x1 = pos1[1]
        x2 = pos2[1]
        y1 = pos1[0]
        y2 = pos2[0]
        pos1vak = rooster[y1][x1]
        pos2vak = rooster[y2][x2]
        rooster[y1][x1] = pos2vak
        rooster[y2][x2] = pos1vak
    return rooster


def next_generation(
    population: list,
    top_ammount: int,
    multiplier: int,
    vakken: list,
    dagen: int,
    daguuren: int,
    mutatie_rate: int,
):
    population_size = len(population)
    next_population = []
    fault = []
    top_population = get_top_populations(population, top_ammount)
    if top_ammount * multiplier > population_size:
        multiplier = floor(population_size / top_ammount)
    wildcards = population_size - (top_ammount * multiplier)

    for i in range(len(top_population)):
        next_population.append(top_population[i])

    for _ in range(multiplier - 1):
        for i in range(len(top_population)):
            rooster = top_population[i][1]
            new_rooster = mutate(rooster, mutatie_rate)
            fitness, tempfault = roosterfitness.calc_fitness(rooster, vakken)
            for j in range(len(tempfault)):
                fault.append(tempfault[j])
            new_item = [fitness, new_rooster, fault]
            fault = []
            next_population.append(new_item)

    for _ in range(wildcards):
        new_rooster = roostergen.gen_rooster(vakken, dagen, daguuren)
        fitness, tempfault = roosterfitness.calc_fitness(new_rooster)
        for j in range(len(tempfault)):
            fault.append(tempfault[j])
        new_item = [fitness, new_rooster, fault]
        fault = []
        next_population.append(new_item)

    return next_population
