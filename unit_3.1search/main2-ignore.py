import random
from workerant import SearchAgent, WorkerAnt
from tile import MapTile

# Create NxN map and place a sugar cube on the map
m = 5
n = 5

sugarCube = (random.randint(0, m-1), random.randint(0, n-1))
print("Sugar cube location: ", sugarCube)

map = []

for x in range(m):
    for y in range(n):
        setSugarCube = False
        # Condition for adding sugar
        if sugarCube == (x,y):
            setSugarCube = True
        map.append(
            # MapTile(m, n, setSugarCube)
            MapTile(x, y, sugarCube == (x,y))
        )

# Create the ant placed on the start
ant_1 = WorkerAnt(0, 0)

# Create the ant placed on any location
# ant_1 = SearchAgent(random.randrange(5), random.randrange(5))

# Convert the x, y coordinate to the index
ant_loc = ant_1.curX * m + ant_1.curY
print("Current ant location at {}".format(ant_loc))

# Let the ant search for the sugar cube on the map
for tile in map[ant_loc:]:
    # print(tile.posX)
    if ant_1.checkForSugar(tile):
        print("Agent run successful!")
        break
    else:
        ant_1.move(tile.posX + 1, tile.posY + 1)
