class Fitness:
    def __init__(self, targetString, numPerPopulation):
        self.targetString = targetString
        self.numPerPopulation = numPerPopulation

    def computeFitness(self, population, strings):
        totalFitness = 1
        targ = self.targetString

        for i, monkey in enumerate(population):
            fitness = 0
            for j, ch in enumerate(strings[i]):
                if targ.count(ch) > 0:
                    fitness += 1
                    if targ[j] == ch or targ.count(ch) == strings[j].count(ch):
                        fitness += 5

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
