class MapTile:
    def __init__(self, posX, posY, hasSugar):
        self.posX = posX
        self.posY = posY
        # you can add other properties for
        self.hasSugar = hasSugar

    def __str__(self):
        str = "{}:{} - {}".format(self.posX, self.posY, self.hasSugar)
        return str