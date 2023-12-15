def isValidSudoku(self, board) -> bool:
        cols= collections.defaultdict(set)
        rows= collections.defaultdict(set)
        square= collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c]=="."):
                    continue
                if(board[r][c] in rows[r] or
                 board[r][c] in cols[c] or
                  board[r][c]  in square[(r//3,c//3)]):
                  return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
