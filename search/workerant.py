class WorkerAnt:
    def __init__(self, curX, curY):
        self.curX = curX
        self.curY = curY

    def move(self, newX, newY):
        self.curX = newX
        self.curY = newY

    def checkForSugar(self, tile):
        if tile.hasSugar:
            print("Ant found the sugar. Time to find the queen")
        else:
           print("No sugar on tile {},{} , moving on...".format(tile.posX, tile.posY))
        
        return tile.hasSugar