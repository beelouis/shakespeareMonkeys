from Monkey import Monkey
from Fitness import Fitness
from Reproducer import Reproducer

def init(popSize, length):
    population = []
    for i in range(popSize):
        m = Monkey(i, length)
        m.setRanChrom()
        population.append(m)

    return population

def iterateGeneration(population, generationCount):
    print("==========================================================================")
    print("==========================================================================")
    print("==========================================================================")
    print("==========================================================================")
    print("Generation:", generationCount)
    return list([monkey.typeString() for monkey in population])
targetString = "hello"
numMonkeys = 50
numPerPopulation = round(numMonkeys / 2)
numGenerations = 200

Pc = 0.8
Pm = 0.01

population = init(numMonkeys, len(targetString))
fitness = Fitness(targetString, numPerPopulation)
reproducer = Reproducer(Pc, Pm)

for i in range(numGenerations):
    gen = iterateGeneration(population, i)
    print("Output: ", gen, "\n")
    if targetString in gen:
        print("String found!")
        break

    fittest = fitness.computeFitness(population, gen)
    children = reproducer.reproduce(fittest)

    population = fittest + children

    for i, monkey in enumerate(population):
        monkey.setLabel(i)
