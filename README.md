# Python_Make_your_own_bingo
A python program that allows you to create a bingo board automatically and pseudo-randomly from txt files containing the information you want on your board. Customizable with personal shoutouts and easy to modify to suit your own needs. 

The following improvements could be implemented 
-Could format bingo board (see function formatBingo)
-Can round to nearest square root of number of squares (that way you can have free squares)
-Better graphics

Originally made in the context of bingo for the annual uOttawa/Carleton panda game

Uses tkinter python standard module to create labels in a type of grid 
Further info on functions: https://effbot.org/tkinterbook/grid.htm 

NOTE:
You need to have the files with your info in the same repo as the bingo file. No need to type them in as .txt


Formatting improvements
#function to format the info into a bingo table, using tkinter module
#parameter is array with info to put into grid, number of grids (number to be squared)
#if grid is not filled there will just be empty space in middle 
#always start top left corner for numbering (4x4 example)
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
"""
3x3 example
1  2  3
8  9  4
