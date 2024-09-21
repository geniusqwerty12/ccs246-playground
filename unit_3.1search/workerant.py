class WorkerAnt:
    def __init__(self, curX, curY):
        self.curX = curX
        self.curY = curY
        print("Ant starts searching on tile ({},{})".format(self.curX, self.curY))

    
    def move(self, newX, newY):
        self.curX = newX
        self.curY = newY

    def checkForSugar(self, tile):
        if tile.hasSugar:
            print("Ant found the sugar on tile ({}-{}). Time to find the queen!".format(tile.posX, tile.posY))
        else:
           print("No sugar on tile ({}-{}), moving on...".format(tile.posX, tile.posY))
        
        return tile.hasSugar