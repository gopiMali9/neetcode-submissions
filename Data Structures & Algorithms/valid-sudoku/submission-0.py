class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        valid = [str(i) for i in range(10)]+['.']

        print(valid)

        for i in board:
            for j in i:
                if j not in valid:
                    return False
                    
                if j != '.' and i.count(j) > 1:
                    return False

        for i in zip(*board):
            for j in i:
                if j not in valid:
                    return False
                    
                if j != '.' and i.count(j) > 1:
                    return False
        
        step = 0

        for i in range(3,10,3):
            grid = []
            count = 0
            for k in zip(*board[step:i]):
                grid.extend(k)
                count += 1

                if count %3 == 0 :
                    for l in grid:
                        ######
                        if l not in valid:
                            return False
                    
                        if l != '.' and grid.count(l) > 1:
                            return False
                    grid = []
            step = i
        
        return True




        




