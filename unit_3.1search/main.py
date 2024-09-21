import random
from anthill import AntHill
from workerant import WorkerAnt

m = 5
n = 5

# Create the environment
antHill = AntHill(m, n)

# Create an agent located from the start
# ant_1 = WorkerAnt(0, 0)
# antHill.startSearch(ant_1)

# Create another ant with a starting position being random
ant_2 = WorkerAnt( random.randint(0, m-1), random.randint(0, n-1) )
antHill.startSearch(ant_2)