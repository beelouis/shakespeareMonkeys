import random
from Monkey import Monkey

class Reproducer:
    def __init__(self, Pc, Pm):
        self.Pc = Pc
        self.Pm = Pm

    def reproduce(self, parents):
        children = []
        for i, parent in enumerate(parents):
            nextIndex = (i+1)%len(parents)
            couple = [parent, parents[nextIndex]]
            if random.random() < self.Pc:
                child = self.recombine(couple)
            else:
                child = couple[random.randint(0, 1)].duplicate()
            children.append(child)
        children = self.mutate(children)
        return children

    def recombine(self, parents):
        p1 = parents[0]
        p2 = parents[1]
        length = len(parents[0].chrom)
        locus = round(length / 2)

        childChrom = p1.chrom[:locus] + p2.chrom[locus:]
        childLabel = int(str(p1.label) + str(p2.label))
        child = Monkey(childLabel, p1.stringLength)

        child.setChrom(childChrom)
        child.

        setWeights = [i*j for weight in child.]

        # weights = [w for i in range(ln)]
        return child

    def mutate(self, children):
        for child in children:
            for index, bit in enumerate(child.chrom):
                if random.random() < self.Pm:
                    child.chrom[index] = 1 if bit == 0 else 0

        return children
