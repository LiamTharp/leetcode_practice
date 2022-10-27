def findBall(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[int]
    """
    
    out = [-1 for _ in enumerate(grid[0])]
    
    for idx, _ in enumerate(grid[0]):
        
        row, col = 0, idx
        
        while row < len(grid):
        
            if col == 0 and grid[row][col] == -1:
                break
            
            if col == len(grid[0]) - 1 and grid[row][col] == 1:
                break
            
            val = grid[row][col]
            
            if abs(grid[row][col] + grid[row][col + val]) != 2:
                break
            
            if row == len(grid) - 1:
                out[idx] = col + val

            row, col = row + 1, col + val

    print(out)

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1]]

print(findBall(grid))