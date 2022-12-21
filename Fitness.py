class Fitness:
    def __init__(self, targetString, numPerPopulation):
        self.targetString = targetString
        self.numPerPopulation = numPerPopulation

    def computeFitness(self, population, generationOfStrings):
        totalFitness = 0
        for i, monkey in enumerate(population):
            fitness = 0
            for ch in generationOfStrings[i]:
                fitOfCh = 1 if self.targetString.count(ch) > 0 else 0
                fitness += fitOfCh
            totalFitness += fitness
            monkey.setFitness(fitness)
        print("total fitness for this generation:", totalFitness)
        selected = self.orderAndSelect(population)
        return selected

    def orderAndSelect(self, population):
        orderedList = sorted(population, key = lambda x:x.fitness, reverse = True)
        selected = []
        for i in range(self.numPerPopulation):
            selected.append(orderedList[i])
        return selected
