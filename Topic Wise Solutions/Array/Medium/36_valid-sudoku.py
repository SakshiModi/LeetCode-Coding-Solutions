class Solution:
    def isValidSudoku(self, board):
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        blocks=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                x=((i//3)*3)+(j//3)
                if board[i][j] in blocks[x]:
                    return False
                else:
                    blocks[x].add(board[i][j])
        return True
