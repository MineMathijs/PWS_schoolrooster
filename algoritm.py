
from collections import namedtuple
from functools import partial
from random import choices, randint, randrange
import random
from typing import Callable, List, Tuple
import dbfunc

# dbfunc.show_all()

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutateFunc = Callable[[Genome], Genome]
Thing = namedtuple('Thing', ['name', 'weight', 'value'])

things = [
    Thing('laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192),
    Thing('Mints', 5, 25),
    Thing('Socks', 10, 38),
    Thing('Tissues', 15, 80),
    Thing('Phone', 500,200),
    Thing('Baseball cap', 100, 70)
]

more_things = [
    Thing('Mints', 5, 25),
    Thing('Socks', 10, 38),
    Thing('Tissues', 15, 80),
    Thing('Phone', 500,200),
    Thing('Baseball cap', 100, 70)
]

# generate genome
def generate_genome(length: int) -> Genome:
    return choices([0,1], k=length)

# generate population
def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

# fitnes function
def fitness(genome: Genome, things, weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and thing must be same length")
    
    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0
    return value

#selection
def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for fenome in population],
        k=2
    )

# cross over
def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome,Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of the same length")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, lenght-1)
    return a[0:p] + b[p:], b[0:p] + b[p:]

# mutation
def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome


#evolution
def run_evolution(
    populate_func: PopulateFunc,
    fitness_func: FitnessFunc,
    fitnesss_limit: int = 1310,
    selection_func: SelectionFunc = selection_pair,
    crossover_func: CrossoverFunc = single_point_crossover,
    mutation_func: MutateFunc = mutation,
    generation_limit: int = 100
) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)
        
        if fitness_func(population[0]) >= fitnesss_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) -1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )

    return population, i

population, generations = run_evolution(
    populate_func=partial(
        generate_population, size=10, genome_length=len(things)
    ),
    fitness_func=partial(
        fitness, things=things, weight_limit = 3000
    ),
    fitnesss_limit=740,
    generation_limit=100
)

def genome_to_things(genome: Genome, things):
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing.name]

    return result


print(f"number of generations: {generations}")
print(f"best solution: {genome_to_things(population[0], things)}")