from HexGrid import HexGrid
from Element import *

BOARD_INDEX_ERROR = "Board index out of range"

class Board:
    """
    Class to represent a board for a Sigmar's Garden game.
    It handles the organization and placement of the marbles on the board.
    """

    def __init__(self):
        self.board = list()

        for y in range(11):
            self.board.append(list())
            for x in range(11):
                self.board[y].append(HexGrid(x, y))

        self.metalList = ["Lead", "Tin", "Iron", "Copper", "Silver", "Gold"]

        self.clearMetalNum = 0

    def getElement(self, x, y):
        """
        Get the element from the given hexgrid, if anything.
        """
        if self.isValid(x, y):
            return self.board[y][x].getElement()

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def setElement(self, x, y, element):
        """
        Assign the element to the given hexgrid.
        """
        if self.isValid(x, y):
            self.board[y][x].setElement(element)

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def removeElement(self, x, y):
        """
        Remove the element, if anything, from the given hexgrid.
        """
        if self.isValid(x, y):
            self.board[y][x].removeElement()

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def clear(self, elementName):
        """
        Clear up the current metal when it got matched and get the next one.
        """
        if elementName == self.metalList[self.clearMetalNum]:
            self.clearMetalNum += 1

    def getMetalToClear(self):
        """
        Get the information on which metal should be matched first.
        """
        if self.clearMetalNum >= len(self.metalList):
            return None

        return self.metalList[self.clearMetalNum]

    @staticmethod
    def isValid(x, y):
        """
        Get the given position and verfy whether it is valid and is on a board.
        """
        return 0 <= x <= 10 and max(x-5, 0) <= y <= min(x+5, 10)

print(help(Board))