class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowset = set()
        colset = set()
        boxset = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]

                #check row
                if (i,num) in rowset:
                    return False
                rowset.add((i,num))

                #check column
                if (j,num) in colset:
                    return False
                colset.add((j,num))

                #check 3*3  rows

                box = (i//3,j//3)
                if (box,num) in boxset:
                    return False
                boxset.add((box,num))
        return True
                           

        