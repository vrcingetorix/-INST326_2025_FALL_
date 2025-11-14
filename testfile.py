#testing 123 
# testinggg 

#Sahith's update


#Michael was here 


#Lauren Pierre-Louis made a change



#Sahith's code (Ship Location)


import random


def ship_location(grid):
    empty_cells = []
    total_rows = len(grid)
    total_columns = len(grid[0])
    
    for row in range(len(grid)):
        for col in range(total_columns):
            if grid[row][col] == 0:
                empty_cells.append((row, col))
    
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = 1
            
    return grid


example_grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# The 0 represents grids that are empty, 1 represents grid with ship placed


new_grid = ship_location(example_grid)
for row in new_grid:
    print(row)

#Testing Function

