class HexGrid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.element = None

    def getPosition(self):
        return self.x, self.y

    def setElement(self, element):
        self.element = element

    def getElement(self):
        return self.element

    def removeElement(self):
        self.element = None

    def getNeighborPositions(self):
        x = self.x
        y = self.y

        return (
            (x-1, y-1),
            (x  , y-1),
            (x+1, y  ),
            (x+1, y+1),
            (x  , y+1),
            (x-1, y  )
        )

    def isOccupied(self):
        return self.element != None
