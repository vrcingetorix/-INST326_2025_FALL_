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
# form of a coordinatoes for a cell, which is the the number of the row and column separated by columns in parentheses. The
# function returns a string indicating whether the player hit a ship or not.
# ○ Inputs: player position and opposition coordinates ( both tuples )
# ○ Outputs: would be a string value of either attack, sink, or miss

def attack(grid):

    attack_coordinates = input("Enter attack coordinates, with row and col separated by a space: ")

    cell = grid[row][col]

    if cell == 2 or cell == -1:
        return "This position has already been attacked!" # prevents duplicate attacks
    
    if cell == 1:
        grid[row][col] = 2
        return "Hit!" # this marks the attack as a hit
    
    if cell == 0:
        grid[row][col] = -1
        return "Miss!" # marks as a miss
    
    