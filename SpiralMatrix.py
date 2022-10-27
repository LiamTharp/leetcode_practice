def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    m = len(matrix)
    n = len(matrix[0])

    size = m * n
    
      
    used_coords = []
            
    coords = [0, 0]
    path = []
    direction = [0, 1]
    
    while len(path) < size:
        
        used_coords.append(coords)

        path.append(matrix[coords[0]][coords[1]])
        
        matrix[coords[0]][coords[1]] = 101

        nrow, ncol = coords[0] + direction[0], coords[1] + direction[1]

        if (0 <= nrow < len(matrix)) and (0 <= ncol < len(matrix[0])) and (matrix[nrow][ncol]) != 101:
            coords[0], coords[1] = nrow, ncol
        else:
                direction[0], direction[1] = direction[1], -direction[0]
                coords[0], coords[1] = coords[0]+direction[0], coords[1]+direction[1]
    return path




            


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
    