#testing 123 
# testinggg 

<<<<<<< HEAD
# paulina testing
=======
#Sahith's update


#Michael was here 


#Lauren Pierre-Louis made a change
<<<<<<< HEAD
>>>>>>> 412d064df4b7670b7c3bdad06e3d9517c388aaba
=======



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

>>>>>>> 9118361facd72c63173d876c17ff2e868e53dcd3

# Paulina's function - attack mechanism

# Attack Mechanism - The game must take input from the player as a guess to where to attack the opponent. The input is in the
# form of a coordinatoes for a cell, which is the the number of the row and column as two integers. The
# function returns a string indicating whether the player hit a ship or not and then marks the cell as being attacked already.
# ○ Inputs: desired coordinates for attack
# ○ Outputs: would be a string value of either attack or miss

fake_grid = [
    [0, 0, 1]
    [0, 1, 0]
    [1, 0, 0]
]

def attack(grid):
    try:
        row = int(input("Enter the row you want to attack: "))
        col = int(input("Enter the column you want to attack: "))
    except ValueError:
        return "Invalid input."
    
    valid_row = 0 <= row < len(grid)
    valid_col = 0 <= col < len(grid[0])

    if not (valid_row and valid_col):
        return "Coordinates out of range." # checks bounds

    cell = grid[row][col]
    previous_attack = (cell == 2) or (cell == -1)

    if previous_attack:
        return "This position has already been attacked!" # prevents duplicate attacks    
    
    ship = (cell == 1)
    
    if ship:
        grid[row][col] = 2
        return "Hit!" # this marks the attack as a hit
    else:
        grid[row][col] = -1
        return "Miss!" # marks as a miss
    

    
