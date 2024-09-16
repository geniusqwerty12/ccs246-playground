from anthill import AntHill
from workerant import WorkerAnt

m = 5
n = 5

# Create the environment
antHill = AntHill(m, n)

# Create an agent located from the start
ant_1 = WorkerAnt(0, 0)

antHill.startSearch(ant_1)