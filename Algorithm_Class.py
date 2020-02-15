import random 
import numpy as np

np.random.seed(42)
class Genetic_Algorithm:
    
    def __init__(self, Npop=50, Nchrom = 15, PC=None, PM=None):
        self.Npop = Npop
        self.Nchrom = Nchrom
        self.PC = PC
        self.PM = PM
        self.size = (self.Npop,self.Nchrom)
        
    def init_pop(self,s=None):
        s = self.size if s == None else s
        self.pop = np.random.randint(0,2,s)
        return np.random.randint(0,2,s)
    
    def fitness(self, chroms = None):
        chroms = self.pop if chroms == None else chroms     
        ex = np.array([sorted(list(range(chroms.shape[1])), reverse=True)])  
        squarer = lambda x: x ** 2
        vfunc = np.vectorize(squarer)
        
        ch_fit = np.dot(chroms, vfunc(ex).reshape((-1,1)))
    
        return chroms
    def train(self, gens = 1):
        self.init_pop()
        ch_fit = self.fitness()
        return ch_fit