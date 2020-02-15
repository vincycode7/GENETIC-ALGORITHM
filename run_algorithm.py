from Algorithm_Class import Genetic_Algorithm

test = Genetic_Algorithm(Npop=50, Nchrom = 15, PC = 0.7, PM = 0.01)
print('the total fitness of population: ',test.train()reset)