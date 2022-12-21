import random
from Monkey import Monkey

class Reproducer:
    def __init__(self, Pc, Pm):
        self.Pc = Pc
        self.Pm = Pm

    def reproduce(self, parents):
        children = []
        for i, parent in enumerate(parents):
            couple = [parent, parents[(i+1) % len(parents)]]
            if random.random() < self.Pc:
                child = self.recombine(couple)
            else:
                child = couple[random.randint(0, 1)]
            children.append(child)
        children = self.mutate(children)

        return children

    def recombine(self, parents):
        length = len(parents[0].chrom)
        locus = round(length / 2)
        childChrom = parents[0].chrom[:locus] + parents[1].chrom[locus:]
        childLabel = int(str(parents[0].label) + str(parents[1].label))
        child = Monkey(childLabel, parents[0].stringLength)
        child.setChrom(childChrom)
        return child

    def mutate(self, children):
        for child in children:
            for index, bit in enumerate(child.chrom):
                if random.random() < self.Pm:
                    child.chrom[index] = 1 if bit == 0 else 0

        return children
