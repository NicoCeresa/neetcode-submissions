class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for each row, col, box keep track of what Ive seen
        # for box check if ind+1, 2 % 3 in seen
        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)
        isValid = True
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == ".":
                    continue
                
                if ((board[x][y] in row[x]) or 
                    (board[x][y] in col[y]) or 
                    (board[x][y] in box[(x // 3, y // 3)])):
                    return False
                row[x].add(board[x][y])
                col[y].add(board[x][y])
                box[(x // 3, y // 3)].add(board[x][y])
        return True

