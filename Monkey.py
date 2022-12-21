import random

class Monkey:
    def __init__(self, label, stringLength):
        self.label = label
        self.stringLength = stringLength
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def setRanChrom(self):
        self.chrom = [random.randint(0, 1) for i in range(len(self.alphabet))]
        self.setVocabFromChrom()

    def setChrom(self, chrom):
        self.chrom = chrom
        self.setVocabFromChrom()

    def setVocabFromChrom(self):
        self.vocab = [ch for i, ch in enumerate(self.alphabet) if self.chrom[i] == 1]

    def setFitness(self, fitness):
        self.fitness = fitness

    def setPropFitness(self, propFitness):
        self.propFitness = propFitness

    def setLabel(self, label):
        self.label = label

    def typeString(self):
        string = ""
        for i in range(self.stringLength):
            string += self.vocab[random.randint(0, len(self.vocab)-1)]
        return string
