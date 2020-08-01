from HexGrid import HexGrid
from Element import *

BOARD_INDEX_ERROR = "Board index out of range"

class Board:
    def __init__(self):
        self.board = list()

        for y in range(11):
            self.board.append(list())
            for x in range(11):
                self.board[y].append(HexGrid(x, y))

        self.metalList = ["Lead", "Tin", "Iron", "Copper", "Silver", "Gold"]

        self.clearMetalNum = 0

    def getElement(self, x, y):
        if self.isValid(x, y):
            return self.board[y][x].getElement()

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def setElement(self, x, y, element):
        if self.isValid(x, y):
            self.board[y][x].setElement(element)

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def removeElement(self, x, y):
        if self.isValid(x, y):
            self.board[y][x].removeElement()

        else:
            raise IndexError(BOARD_INDEX_ERROR)

    def clear(self, elementName):
        if elementName == self.metalList[self.clearMetalNum]:
            self.clearMetalNum += 1

    def getMetalToClear(self):
        if self.clearMetalNum >= len(self.metalList):
            return None

        return self.metalList[self.clearMetalNum]

    @staticmethod
    def isValid(x, y):
        return 0 <= x <= 10 and max(x-5, 0) <= y <= min(x+5, 10)
