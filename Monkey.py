import random

class Monkey:
    def __init__(self, label, stringLength):
        self.label = label
        self.stringLength = stringLength
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def setChrom(self, chrom):
        # real value for chromosome, between 0 and maxWeight
        self.chrom = chrom

    def setVocabFromChrom(self):
        self.vocab = [ch for i, ch in enumerate(self.alphabet)]

    def setWeights(self, weights):
        self.weights = weights
        self.propWeights = [weight/self.sumWeights for weight in self.weights]
        self.vocabWeighted = dict({ch : pWeight for ch in self.alphabet for pWeight in self.propWeights})

    def setDeltaWeights(self, deltaWeights):
        self.deltaWeights = [deltaW for deltaW in deltaWeights]

    def modifyWeights(self):
        self.weights = [w * dw for w in self.weights for dw in self.deltaWeights]

    def setFitness(self, fitness):
        self.fitness = fitness

    def setLabel(self, label):
        self.label = label

    def duplicate(self):
        m = Monkey(self.label, self.stringLength)
        m.setChrom(self.chrom)
        m.setWeights(self.weights)
        m.setDeltaWeights(self.deltaWeights)
        m.modifyWeights()
        return m

    def typeString(self):
        string = ""
        orderedWeights = sorted(self.vocabWeighted.items(), key = lambda x:x[1])
        while (len(string) < self.stringLength):
            r = random.random()
            s = 0
            for orderedCh in orderedWeights:
                s += orderedCh[1]
                if s > r:
                    string += orderedCh[0]
                    break
        return string
