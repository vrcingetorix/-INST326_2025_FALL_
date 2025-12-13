# Battleship Rumble
## repo: -INST326_2025_FALL_

## TODO: 

### Your documentation should include
Welcome to Battlship Rumble! This is our spin on the classic Battleship game
with extra features to make a text-based as fun as it can be. The only files in
our repository are .gitignore, our license, the readme.md, and the actual file
with the game, testfile.py.

To run the game on Windows, go to either your VSCode terminal or the Windows 
Powershell terminal and type "python testfile.py" in the command line. Once you 
run it, the game will welcome you, and you will have to type in your name.

- Note: please do not type any extra spaces or anything other than one the prompt
is asking.

Then the game begins with your turn. It prints the CPU's grid and your grid, both
are 10x10 and the cells that say "W" mean "water" or rather empty cells. However,
the CPU's grid shows only water so that its ship locations are secret to you, but
they are there!

You will be given 20 Command Points, a list of actions, and a prompt to pick your
action. Each action you take subtracts from the given command points in each round.
To choose an action, simply type the corresponding number in the prompt box, and
nothing else. 

If you choose attack, it'll be followed by two separate prompts asking
for which row and column you would like to attack, and for each of these just type
a single number. Once you enter, this will return whether you've hit, missed, or
something in that cell. Press enter for the next round and so on. A hit on either grid
will become an "X" and a miss will become a "O".

If you choose defend, itll ask for the row and column you are wanting to defend. 
Defend hides that cell from the opponent for a round. So, if CPU happens to attack
the cell you hid, itll register as a miss for it.

If you choose move, it will print a list of your ships for you, and you must enter
the corresponding list number for the ship you want to move. Then it will ask you
for the direction in which you want to move it, and for this as well just type
your response exactly as the prompt asks you to.

The fun one! If you choose special attack, it  will ask you for a row and column
again. This action can only be used once in the entire game, so choose wisely!
It creates a 3x3 blast attack around the cell you chose.

Finally, if you choose scan, it will prompt you for a row and column again, and
asks whether you want to check one space diagonally by typing "d" or one space
vertically or horizonally by typing "v". It will return with a cryptic message
letting you know whether there is a ship nearby or not.

To win, sink the CPU's entire fleet. 

# Bibliography
    Clipart Library. (2025). Clipart-Library.com. https://clipart-library.com/2023/445-4453395_png-royalty-free-download-battleship-clipart-battleship-clipart.pngAn image of a battleship used in our presentation.

    Dreamstime.com. (2025). Dreamstime.com. https://thumbs.dreamstime.com/b/battleship-icon-cartoon-style-illustration-vector-web-85897705.jpgsecond image of a battleship used in our presentation

    Philip F. (2021, October 2). Strategies in battleship. Board & Card Games Stack Exchange. https://boardgames.stackexchange.com/questions/56427/strategies-in-battleshipsome inspiration we used to determine how to go about making our game and what rules/strategies to implement



‌   

### In the table, list all methods and functions that are being claimed by any member of the group in fulfillment of item 7 above. Only list the techniques that are being claimed in fulfillment of item 7d (for example, three functions may contain f-strings, but only one member of the group can claim f-strings and they should only be listed once in the table).

    - Please make sure your table meets the following specifications:

    - Do not list classes or other units of code in the table, only functions and methods.

    - Only one function or method per row.

    - Only one primary author per function or method.

    - Please list as many techniques in a given row as you are claiming credit for in that function or method (for example, method foo might have two techniques, while method bar has zero; that's totally fine).

    - A given technique should only appear once in the table.
