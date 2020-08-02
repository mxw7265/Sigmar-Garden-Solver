class HexGrid:
    """
    Class to represent a single hexagon grid for a Sigmar's Garden game.
    It handles the organization and placement of the marbles on the grid.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.element = None

    def getPosition(self):
        """
        Get the position and return it as tuple (x, y)
        """
        return self.x, self.y

    def setElement(self, element):
        """
        Set the element into this hexgrid.
        """
        self.element = element

    def getElement(self):
        """
        Get the element from this hexgrid, if anything.
        """
        return self.element

    def removeElement(self):
        """
        Removes element from this hexgrid, if anything.
        """
        self.element = None

    def getNeighborPositions(self):
        """
        Returns all neighbor hexgrid based on this hexgrid's coordinate.
        """
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
        """
        Check whether this hexgrid is occupied or not.
        """
        return self.element != None
