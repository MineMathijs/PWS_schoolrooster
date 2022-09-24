from collections import namedtuple
from random import choices
from typing import List
import dbfunc

dbfunc.show_all()

Genome = List[int]
Population = List[Genome]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

# generate genome
def generate_genome(length: int) -> Genome:
    return choices([0,1], k=length)

# generate population
def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

# fitnes function
def fitness(genome: Genome, things: [Thing], wheight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and thing must be same length")
    
    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > wheight_limit:
                return 0
    return value