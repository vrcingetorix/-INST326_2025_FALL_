"""     
    - NOTES -
from paulina to lauren - i think u need boundary checks prolly

general: 
    1. we need to finish the game loop so its functional
    2. if name = main whatever
    3. need special attack and move functions (can only use each once per game)
    4. what are we doing with the command points? is defend just if the enemy hits near ur ship but misses?
    5. argparse
most important thing for now is to make at least working demo - tweaks can be made later

special_attack - michael
defend - lauren
hidden - michael
cpu attack - sahith - place inside player class, cpu is a player, self and opponent, account for cells that have already been
previously attacked, account for grid size, change values of cells after attacks. print message for human player (refer to 
attack function for inspo)
finish game loop/main menu - paulina
"""



import random

grid_size = 10

# ship class - paulina
class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = set(positions)
        self.hits = set()
    
    def record_hit(self, coord):
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
        self.previous_attacks = set()
        self.defend = False

    def assign_ships(self, num_single = 3, num_multi = 2): # assigns different types of ships, can be edited later
        for i in range(num_single):
            self.grid, pos = ship_location(self.grid) # single cell ship
            if pos: 
                ship = Ship(f"Single ship {i+1}", [pos])
                self.ships.append(ship)

        for i in range(num_multi):
            ship_size = random.choice([2, 3, 4, 5])
            positions = place_ships(self.grid, ship_size)
            ship = Ship(f"Multi ship {i+1}", positions)
            self.ships.append(ship)


#Sahith's code (Ship Location + valid bounds + special attack)


def ship_location(grid):
    empty_areas = []
    rows = len(grid)
    columns = len(grid[0])
    
    for row in range(len(grid)):
        for col in range(columns):
            if grid[row][col] == 0:
                empty_areas.append((row, col))
                
    if len(empty_areas)>0:
        row, col = random.choice(empty_areas)
        grid[row][col] = 1
        return grid, (row, col)
    elif len(empty_areas) == 0:
        return grid, None
         
def empty_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return grid

# edit 2
def valid_bounds(row, col, size=grid_size):
    return (0 <= row < size) and (0<= col < size)
    
def special_attack(player, enemy_grid):
    if player.special_attack_used:
        return f'The special attack has already been used, {player.name}'
    row_input = input("Enter your center row")
    col_input = input("Enter your center column")
    
    try:
        r = int(row_input)
        c = int(col_input)
    except ValueError:
        return "Invalid input"
    if not valid_bounds(r, c):
        return f' The coordinates ({r}, {c}) are out of range'
    
    hits = 0
    r_offset = [-1, 0, 1]
    c_offset = [-1, 0, 1]
    for rs in r_offset:
        for cs in c_offset:
            result_row = r+rs
            result_col = c+cs
            
            if not valid_bounds(result_row, result_col, grid_size):
                continue
            
            current_val = enemy_grid[result_row][result_col]
            if current_val ==-1 or current_val == 2:
                continue
            elif current_val == 1:
                enemy_grid[result_row][result_col] = 2
                hits = hits + 1
            else:
                enemy_grid[result_row][result_col] = -1
            
    player.special_attack_used = True
    return f' The player {player.name} used special attack, scoring {hits} hits'

            
        
                
                
                
            
            
            
            
    
            
                
    


    


#Testing Function


# Paulina's function - attack mechanism

# Attack Mechanism - The game must take input from the player as a guess to where to attack the opponent. The input is in the
# form of a coordinatoes for a cell, which is the the number of the row and column as two integers. The
# function returns a string indicating whether the player hit a ship or not and then marks the cell as being attacked already.
# ○ Inputs: desired coordinates for attack
# ○ Outputs: would be a string value of either attack or miss


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
        return {
            f"Hit! {row, col}"
                } # this marks the attack as a hit
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
#Movement Function 

def move(player, ship, direction):
    #directions 
    new_positions = []
    for (rows, cols) in ship.positions:
        if direction == "up":
            row = rows - 1
            col = cols
        elif direction == "down":
            row = rows + 1
            col = cols
        elif direction == "left":
            row = rows
            col = cols - 1
        elif direction == "right":
            row = rows
            col = cols + 1
        else:
            return "Invalid direction"
        
        if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
            return "Out of Bounds"

        cell = player.grid[row][col]
        if cell != 0 and (row, col) not in ship.positions:
            return "Cannot move"
        
        new_positions.append((row, col))
    
    for (row, col) in ship.positions:
        player.grid[row][col] = 0
    
    for (row, col) in new_positions:
        player.grid[row][col] = 1
    
    ship.positions = set(new_positions)
    return "Move successful"
    

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
    

# game loop - paulina

player_name = input("Please enter your name: ")
player = Player(player_name)

cpu = Player("CPU")

player.assign_ships()
cpu.assign_ships()



# need to add more