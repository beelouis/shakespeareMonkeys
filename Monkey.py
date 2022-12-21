import random

class Monkey:
    def __init__(self, label, stringLength):
        self.label = label
        self.stringLength = stringLength
        self.alphabet = "abcdefgh"
        self.genChromosome()

    def genChromosome(self):
        self.chrm = [random.randint(0, 1) for i in range(len(self.alphabet))]
        self.vocab = [ch for i, ch in enumerate(self.alphabet) if self.chrm[i] == 1]
        print("Chromosome for monkey", self.label, self.chrm)
        print("Vocabulary:", self.vocab, "\n")

    def typeStringNaive(self):
        string = ""
        for i in range(self.stringLength):
            string += self.alphabet[random.randint(0, len(self.alphabet)-1)]
        return string

    def typeString(self):
        string = ""
        for i in range(self.stringLength):
            string += self.vocab[random.randint(0, len(self.vocab)-1)]
        return string
