"""     
    - NOTES -

general: 
    1. we need to finish the game loop so its functional
    2. need special attack and move functions (can only use each once per game)
    3. incorporate command points system in game loop
most important thing for now is to make at least working demo - tweaks can be made later

# TODO:
defend - lauren
hidden cpu grid (prints hits and misses only) (in game loop) - michael
finish game loop/main menu (add main menu and messages for the user) - 
print_player_grid (in game loop) -  michael

will remove later test tes test bfvtfhdt dhsrgbrb
"""

import random
import os


#Sahith's valid bounds function

grid_size = 10


def valid_bounds(row, col, size=grid_size):
    '''
    The function checks whether a specific coordinate is in the bounds of the grid
    
    Parameters:
        row (int): checking the row's bound validity
        col (int): checking the column's bound validity
        size (int): the size of the grid
        
    Returns: 
        bool: Marks it as True if the coordinates are within grid parameters; 
        if not, it is False
    '''
    return (0 <= row < size) and (0<= col < size)

def empty_grid(size):
    '''
    Initializes a square grid with zeros in each cell, indicating empty positions
    
    Parameters:
        size (int): width and height of the grid
        
        
    Returns:
        list[list[int]]: It returns a 2d list where each element is 0
    '''
    
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return grid

def print_hidden_grid(grid):
    print(" 0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(f"{i} ", end="")
        for j in grid[i]:
            if j == 2:
                print("X ", end="") 
            elif j == -1:
                print("O ", end="")  
            else:
                print("W ", end="")  
        print()
        
def print_player_grid(grid):
    print(" 0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(f"{i} ", end="")
        for j in grid[i]:
            if j == 1:
                print("S ", end="")  
            elif j == 2:
                print("X ", end="") 
            elif j == -1:
                print("O ", end="")  
            else:
                print("W ", end="")  
        print()

#Sahith's code (Ship Location)


def ship_location(grid):
    '''
    This function places the ship in any single cell on the grid; it analyzes the
    grid and sees whether empty cells, which are cells with a value of 0, exists. If
    this is the case, then the empty cell's value changes from 0 to 1, meaning that it
    is converted to a ship cell. 
    
    Parameters:
        grid (list[list[int]]): This is the ship's placement on the player's grid
    
    Returns:
        tuple: returns the updated grid as integers in a list under a list, and the
        ship's position as a tuple (row, col) or None if the grid's spaces are occupied. 
    '''
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
         

def place_ships(grid, ship_size): # basically like ship_location but for multi-cell ships - paulina
    """
    Places ships of given size and random orientation on the grid.

    Args:
        grid (list): 
        ship_size (int): _description_

    Returns:
        positions (tuple): _description_
    
    Author: Paulina Strunnikova

    """
    size = len(grid)
    placed = False

    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, size-1)
            col = random.randint(0, size - ship_size)
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


# ship class - paulina
class Ship:
    def __init__(self, name, positions):
        """
        Initializes a Ship object with a name and positions, and sets hits to an empty set.

        Args:
            name (_type_): _description_
            positions (_type_): _description_
        """
        self.name = name
        self.positions = set(positions)
        self.hits = set()
    
    def record_hit(self, coord): # - paulina
        if coord in self.positions:
            self.hits.add(coord)

    def sunkeness(self): # paulina
        return self.hits == self.positions
    
    def __repr__(self): # paulina
        return f"{self.name} is at {self.positions}"
    
    
    
# player class - paulina (trying to make it so you can only use a special attack once per game)

class Player:
    def __init__(self, name): 
        self.name = name
        self.special_attack_used = False
        self.grid = [[0]*grid_size for _ in range(grid_size)]
        self.ships = []
        self.previous_attacks = set()
        self.is_defending = False
        self.defended_cell = None
        self.command_points = 20

    def assign_ships(self, num_single = 2, num_multi = 3): # paulina
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

    #Sahith's special attack
    
    def special_attack(self, opponent):
        '''
        This function runs a 3x3 grid attack (emulating a blast radius) according
        to the coordinates that the user enters. 
        
        Parameters:
            opponent: The player object whose grid will be targeted for attack
            
        Returns:
            str: A result message pops up if whether the person hits or it results
            in an error
            
            *Special attack attacks 9 cells in total as it is a 3x3 grid
        '''
        
        
        if self.special_attack_used:
            return f'The special attack has already been used, {self.name}'
        row_input = input("Enter your center row")
        col_input = input("Enter your center column")
            
        try:
            r = int(row_input)
            c = int(col_input)
        except ValueError:
            return "Invalid input"
        if not valid_bounds(r, c):
            return f' The coordinates ({r}, {c}) are out of range'
            # test
        hits = 0
        r_offset = [-1, 0, 1]
        c_offset = [-1, 0, 1]
        for rs in r_offset:
                for cs in c_offset:
                    result_row = r+rs
                    result_col = c+cs
                    
                    if not valid_bounds(result_row, result_col, grid_size):
                        continue
                    
                    current_val = opponent.grid[result_row][result_col]
                    if current_val ==-1 or current_val == 2:
                        continue
                    elif current_val == 1:
                        opponent.grid[result_row][result_col] = 2
                        hits = hits + 1
                    else:
                        opponent.grid[result_row][result_col] = -1
                    
        self.special_attack_used = True
        return f' The player {self.name} used special attack, scoring {hits} hits'
        
    def defend(self,grid): # lauren
        row=0
        col=0
        while(self.grid[row][col]!=1):
            row=int(input("what row is the cell you are defending?"))
            col=int(input("what column is the center of the area you are checking?")) 
            if(self.grid[row][col]!=1): 
                print("There's no ship there. Please select another cell")
                continue
            break
        self.is_defending=True
        self.defended_cell=(row,col)
        return self.grid

# Paulina's function - attack mechanism

# Attack Mechanism - The game must take input from the player as a guess to where to attack the opponent. The input is in the
# form of a coordinatoes for a cell, which is the the number of the row and column as two integers. The
# function returns a string indicating whether the player hit a ship or not and then marks the cell as being attacked already.
# ○ Inputs: desired coordinates for attack
# ○ Outputs: would be a string value of either attack or miss

    def attack(self, opponent):
        
        while True:
            try:
                row = int(input("Enter the row you want to attack: "))
                col = int(input("Enter the column you want to attack: "))
            except ValueError:
                return "Invalid input."
            
            valid_row = 0 <= row < grid_size
            valid_col = 0 <= col < grid_size

            if not (valid_row and valid_col):
                print("Coordinates out of range.") # checks bounds
                continue

            cell = opponent.grid[row][col]
            previous_attacks = (cell == 2) or (cell == -1)

            if (row, col) in self.previous_attacks:
                print("This position has already been attacked!") # prevents duplicate attacks 
                continue
            
            break

        self.previous_attacks.add((row, col))

        cell = opponent.grid[row][col]
            
        ship = (cell == 1)
            
        if ship:
            opponent.grid[row][col] = 2
            print(f"Hit! ({row, col})") # this marks the attack as a hit
        
            for ship in opponent.ships:
                if (row, col) in ship.positions:
                    ship.record_hit((row, col))
                    if ship.sunkeness():
                        return f"{self.name} sunk {ship.name}!"
        else:
            opponent.grid[row][col] = -1
            return f"Miss at ({row, col})" # marks as a miss
        
    def cpu_attack(self, opponent): # paulina
            while True:
                row = random.randint(0, grid_size-1)
                col = random.randint(0, grid_size-1)

                if (row, col) not in self.previous_attacks:
                    break

            self.previous_attacks.add((row, col))

            if opponent.is_defending and (row, col) == opponent.defended_cell:
                opponent.is_defending = False
                opponent.defended_cell = None
                return f"CPU attacked ({row, col}) but it was defended!"

            cell = opponent.grid[row][col]

            if cell == 1:
                opponent.grid[row][col] = 2
                
                for ship in opponent.ships:
                    if (row, col) in ship.positions:
                        ship.record_hit((row,col))
                        if ship.sunkeness():
                            return f"CPU sunk {ship.name}"
                            
                return f"CPU hit {self.name}'s ship at ({row, col})."
            else:
                opponent.grid[row][col] = -1
                return f"CPU missed at ({row, col})!"
    #Movement Function - michael
    def move(self, ship, direction):
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

            cell = self.grid[row][col]
            if cell != 0 and (row, col) not in ship.positions:
                return "Cannot move"
            
            new_positions.append((row, col))
        
        for (row, col) in ship.positions:
            self.grid[row][col] = 0
        
        for (row, col) in new_positions:
            self.grid[row][col] = 1
        
        ship.positions = set(new_positions)
        return "Move successful"       
    

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
    action = action.lower()
    costs = cost_of_action.get(action, 0)
    if points >= costs:
        return points - costs
    else:
        return None


#Lauren 
def scanning(player,grid):            
#     A scanning algorithm will be used to help provide information on ship locations.
#       The algorithm will be able to check its position nearby and predict if ships 
#       are located around. The function will scan the coordinate of its position and opposing ships.
#         It will try to check for ships within a specific range and return a value based on 
#         if the ship is close by or not. 
# Inputs: scanning of position and the enemy ship coordinates ( both tuples ) 
# Output: would be a boolean value to decide whether or not the ship is actually in proximity  

    row=int((input("what row is the center of the area you are checking?")))
    col=int((input("what column is the center of the area you are checking?")))
    dir=(input("Please type 'd' for checking in one space diaginally and 'v' for checking in one space up and down along with left and right"))

    if dir=='d': 
        if grid[row][col]==1:
            print("there is a ship in this area")
            return True 
        elif grid[row+1][col]==1 or grid[row-1][col]==1 or grid[row][col+1]==1 or grid[row][col-1]==1:
            print("there is a ship in this area")
            return True 
        else: 
            print("there is no ship in this area")
            return False
    elif dir=='v':
        if grid[row][col]==1:
            print("there is a ship in this area")
            return True  
        elif grid[row+1][col+1]==1 or grid[row+1][col-1]==1 or grid[row-1][col-1]==1 or grid[row-1][col+1]==1:
            print("there is a ship in this area")
            return True 
        else: 
            print("there is no ship in this area")
            return False
    else: 
        print("The wrong button was pressed")
        
   

    

# game loop - michael





if __name__ == "__main__":
    print("Welcome to Battleship Rumble!")
    player_name = input("Please enter your name: ")
    player = Player(player_name)

    cpu = Player("CPU")
    print("Placing ships...")
    player.assign_ships()
    cpu.assign_ships()
    print("Ships placed. Let the battle begin!")

    while True: 
        os.system('cls')
        
        print(f"{player.name}'s turn.")
        print()
        
        print("CPU's grid:")
        print_hidden_grid(cpu.grid)
        
        print(f"\n{player.name}'s grid:")
        print_player_grid(player.grid)
        
        print(f"\nCommand Points: {player.command_points}")
        print("1. Attack (3 pts)")
        print("2. Defend (2 pts)")
        print("3. Move (1 pt)")
        print("4. Special Attack (5 pts)")
        print("5. Scan (2 pts)")
        
        select = input("Choose your action (1-5): ")
        if select == '1':
            points_used = command_points("attack", player.command_points)
            if points_used is not None:
                player.command_points = points_used
                result = player.attack(cpu)
                print(result)
            else:
                print("Not enough command points for Attack.")
        elif select == '2':
            points_used = command_points("defend", player.command_points)
            if points_used is not None:
                player.command_points = points_used
                player.defend(player.grid)
                print("Defend action executed.")
            else:
                print("Not enough command points for Defend.")
        elif select == '3':
            points_used = command_points("move", player.command_points)
            if points_used is not None:
                player.command_points = points_used
                print("Select a ship to move:")
                for i, ship in enumerate(player.ships):
                    print(f"{i + 1}. {ship.name}")
                try:
                    ship_move = int(input("Enter ship number: ")) - 1
                    direction = input("Enter direction (up, down, left, right): ")
                    result = player.move(player.ships[ship_move], direction)
                    print(result)
                except:
                    print("Not a valid ship selection.")
            else:
                print("Not enough command points for Move action.")
        elif select == '4':
            points_used = command_points("special_attack", player.command_points)
            if points_used is not None:
                player.command_points = points_used
                result = player.special_attack(cpu)
                print(result)
            else:
                print("Not enough command points for special attack action.")
        elif select == '5':
            points_used = command_points("scan", player.command_points)
            if points_used is not None:
                player.command_points = points_used
                scanning(player, cpu.grid)
            else:
                print("Not enough command points for Scan action.")
        else: 
            print("Invalid number selection. Must be between 1-5.")
            
        if all(ship.sunkeness() for ship in cpu.ships):
            print(f"{player.name} wins!")
            break
        
        print("CPU's turn.")
        input("Press Enter to continue...")
        result = cpu.cpu_attack(player)
        print(result)
        
        if all(ship.sunkeness() for ship in player.ships):
            print("CPU wins!")
            break
    print("Game Over!!!")
                

