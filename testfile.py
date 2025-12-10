import random

grid_size = 10

# ship class - paulina
class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = set(positions)
        self.hits = set()
    
    def record_hit(self, coord=0):
        if coord in self.positions:
            self.hits.add(coord)

    def sunkeness(self):
        return self.hits == self.positions
    
    def __repr__(self):
        return f"{self.name} is at {self.positions}"
    
    
def place_ships(grid, ship_size): # basically like ship_location but for multi-cell ships
    size = len(grid)
    placed = False

    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, size-1)
            col = random.randint(0, ship_size-1)
            positions = [(row, col+i) for i in range(ship_size)]
        else:
            row = random.randint(0, size-ship_size)
            col = random.randint(0, size-1)
            positions = [(row+i, col) for i in range(ship_size)]

        if all(grid[r][c] == 0 for r,c in positions): # row, col in positions
            for r,c in positions:
                grid[r][c] = 1
            placed = True
        return positions
    
# player class - paulina (trying to make it so you can only use a special attack once per game)

class Player:
    def __init__(self, name):
        self.name = name
        self.special_attack_used = False
        self.grid = [[0]*grid_size for _ in range(grid_size)]
        self.ships = []

    def assign_ships(self, grid, num_single = 2, num_multi = 1): # assigns different types of ships, can be edited later
        for i in range(num_single):
            self.grid, pos = ship_location(self.grid) # single cell ship
            if pos: 
                ship = Ship(f"Single ship {i+1}, [pos]")
                self.ships.append(ship)

        # gonna add a func for assigning multi ships


#Sahith's code (Ship Location)




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


# Paulina's function - attack mechanism

# Attack Mechanism - The game must take input from the player as a guess to where to attack the opponent. The input is in the
# form of a coordinatoes for a cell, which is the the number of the row and column as two integers. The
# function returns a string indicating whether the player hit a ship or not and then marks the cell as being attacked already.
# ○ Inputs: desired coordinates for attack
# ○ Outputs: would be a string value of either attack or miss

grid = [
    [0, 0, 1],
    [0, 1, 0],
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
    
#Michael's Command Points System

cost_of_action =  {
    "attack": 3,
    "defend": 2,
    "move": 1,
    "special_attack": 5,
    "scan": 2
}
def command_points(action, points):
    """
    Used to update the command point total according to the user's action
    
    Parameters: 
        action (str): chosen action selected by user
        points (int): current command point total
        
    Returns:
        points_updated (int): updated command point total
    """
    for correct in cost_of_action.keys():
        if action.lower() == correct:
            break
    lower = action.lower()
    costs = cost_of_action.get(lower, 0)
    points_updated = max(0, points - costs)
    return points_updated
    
#Lauren 
def Scanning(grid,row, col,attack, ran):
    """A scanning algorithm will be used to help provide information on ship locations.
      The algorithm will be able to check its position nearby and predict if ships 
      are located around. The function will scan the coordinate of its position and opposing ships.
        It will try to check for ships within a specific range and return a value based on 
        if the ship is close by or not. 
Inputs: scanning of position and the enemy ship coordinates ( both tuples ) 
Output: would be a boolean value to decide whether or not the ship is actually in proximity  
ran=range
""" 
    if attack == grid[row][col]:
        return True 
    elif grid[row+ran][col] == 1:
        return True
    elif grid[row-ran][col]== 1: 
        return True
    elif grid[row][col+ran] == 1:
        return True 
    elif grid[row][col-ran] == 1:
        return True
    else: 
        return False