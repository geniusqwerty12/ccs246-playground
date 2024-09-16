import random
from tile import MapTile

class AntHill:
    map = []

    # Creating the environment would mean the following
    # generate the location of the sugar cube
    # creating the tile map list
    def __init__(self, m, n):
        self.m = m
        self.n = n

        sugarCube = (random.randint(0, m-1), random.randint(0, n-1))
        print("Sugar cube was placed by the big hand at {}".format(sugarCube))
        for x in range(m):
            row = []
            for y in range(n):
                setSugarCube = False
                if sugarCube == (x,y): setSugarCube = True
                row.append(
                    MapTile(x, y, setSugarCube)
                    # or
                    # MapTile(x, y, sugarCube == (x,y))
                )
            # Add the rows
            self.map.append(row)
        
    # this method executes the search
    # accepts the agent that will analyze the tile map (state space)
    def startSearch(self, ant):
        print("Starting search of the ant for the sugar cube")

        # [ant.curX : ] && [ant.curY:] refers to the starting point of the array depending on the ant's location
        #   start index : "" -> empty means it will go to the last index
        for row in self.map[ant.curX:]:
            for tile in row[ant.curY:]:
                if(ant.checkForSugar(tile)):
                    # Ant found the sugar, stopping the search because there is one sugar cube
                    break
                else:
                    # Update the position of the ant horizontally
                    # follow the mxn grid
                    ant.move(tile.posX, tile.posY + 1)
            else:
                # Update the position of the ant vertically, starting from the left side
                # follow the mxn grid
                ant.move(tile.posX + 1, 0)
                continue
            break