import random

class Fitness:
    def __init__(self, targetString, parentsPerGen):
        self.targetString = targetString
        self.parentsPerGen = parentsPerGen

    def computeFitness(self, population, outputStrings):
        totalFitness = 1
        target = self.targetString

        for i, monkey in enumerate(population):
            fitness = 0
            for j, ch in enumerate(outputStrings[i]):
                if target.count(ch) > 0:
                    fitness += 1
                    if target[j] == ch:
                        fitness += 5
                    if target.count(ch) == outputStrings[j].count(ch):
                        fitness += 5

            totalFitness += fitness
            monkey.setFitness(fitness)
        print("total fitness for this generation:", totalFitness)
        selected = self.orderAndSelect(population)
        return selected

    def orderAndSelect(self, population):
        orderedList = sorted(population, key = lambda x:x.fitness, reverse = False)
        selected = []
        for i in range(self.numPerPopulation):
            selected.append(orderedList[i])
        return selected
