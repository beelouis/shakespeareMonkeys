import random

class Fitness:
    def __init__(self, targetString, numPerPopulation):
        self.targetString = targetString
        self.numPerPopulation = numPerPopulation

    def computeFitness(self, population, generationOfStrings):
        totalFitness = 1
        for i, monkey in enumerate(population):
            monkey.fitness = 0
            for j, ch in enumerate(generationOfStrings[i]):
                if self.targetString.count(ch) > 0:
                    monkey.fitness += 2
                    if self.targetString.count(ch) > 1 and self.targetString.count(ch) < generationOfStrings[i].count(ch):
                        monkey.fitness += 5
                    elif self.targetString.count(ch) == generationOfStrings[i].count(ch):
                        monkey.fitness += 10

                    if self.targetString[j] == ch:
                        print(f"monkey {monkey.label} got the {ch} in the right place at index {j}")
                        monkey.fitness *= 2
            totalFitness += monkey.fitness

        print("total fitness for this generation:", totalFitness)
        for monkey in population:
            monkey.setPropFitness(monkey.fitness / totalFitness)

        selected = self.orderAndSelect(population)
        return selected

    def orderAndSelect(self, population):
        orderedList = sorted(population, key = lambda x:x.propFitness, reverse = False)
#         for monkey in orderedList:
#             print(f"monkey {monkey.label}, fitness: {monkey.propFitness}")

        selected = []
        while (len(selected) < self.numPerPopulation):
            incsum = 0
            r = random.random()
            for monkey in orderedList:
                incsum += monkey.propFitness
                if incsum > r:
                    selected.append(monkey)
                    break

        return selected
