def wordSearch(board, s):
    rows=len(board)
    col= len(board[0])
    path= set()


    def dfs(r,c,i):
        if i==len(word):
            return True
        if (r<0 or c<0 or
            r>=rows or c>=col or s[i]!= board[r][c] or board[r][c] in path):
            return False
        path.add(board[r][c])
        res= ((dfs(r+1,c,i+1) or dfs(r - 1, c, i + 1) or
              dfs(r , c+1, i + 1)) or dfs(r , c-1, i + 1))
        path.remove(board[r][c])
        return res

    for R in range(rows):
        for C in range (col):
            if dfs(R,C,0):
                return True
    return False

word="ABBD"
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(wordSearch(board,word))
