def init(popSize, stringLength):
    population = []
    for i in range(popSize):
        population.append(Monkey(i, stringLength))
    return population

def iterateGeneration(population, generationCount):
    print("==============================")
    print("generation:", generationCount)
    return [monkey.typeString() for monkey in population]

targetString = "hi"
stringLength = len(targetString)
numMonkeys = 10
population = init(numMonkeys, stringLength)
numGenerations = 200

for i in range(numGenerations):
    gen = iterateGeneration(population, i)
    print(gen)
    if targetString in gen:
        print("String found!")
        break
    else:
        print("String not found yet....")
