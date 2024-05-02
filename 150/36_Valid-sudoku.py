class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """


                            # deal with the horizontal rows
        for x in range(9):
            check = self.digitscheck(self,self.makeArray(self,self.getCells(self,[x,0],1,9),board))
            if check == False:
                return False

        return True

    def makeArray(self,cells,board):
        output = []
        while cells:
            coords = cells.pop(0)
            x = coords[0]
            y = coords[1]
            cell = board[x][y]
            if cell != ".":
                output.append(int(cell))
        return output

    def digitscheck(self,digits):
        print(digits)
        silos = []
        for j in range (9):
            silos.append(0)
        for d in digits:
            print(silos[d])
            if silos[d] == 1:
                return False
            silos[d] += 1
        return True


    def getCells(self,corner,width,height):
        x = corner[0]
        y = corner[1]

        cells = []
        coords = []

        for across in range (x,x+width):
            for down in range (y,y+height):
                coords = []
                coords.append(across)
                coords.append(down)
                cells.append(coords)

        return cells



if __name__ == "__main__":
    print(Solution.isValidSudoku(Solution,[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
