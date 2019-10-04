import random
from tkinter import*
import math
'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%PYTHON MAKE-YOUR-OWN-BINGO%%%%%%%%%%%% 
####################################################
#########IMPROVEMENTS##############################

-Could format bingo board (see function formatBingo)
-Can round to nearet square root of number of squares (that way you can have free squares)
-Better graphics
'''
#function to randomise the info
    #parameters: an int (size of bingo card) an array , bool is there personal or no
def randomise(size, info , personal_info, personal):
    b = [] #list to keep track fo values
    for i in range(0, size-1): #have to choose this many squares-1 (don't know personal yet)
        picked=False
        while (picked==False):
        #pick a random number, make sure it hasn't been picked yet
            n=random.randint(0, len(info)-1)
            if (info[n] in b):
                picked=False
            else:
                b.append(info[n]) #put the value into the list
                picked==True
                break
                
    #personal condition or not
                #IMPROVEMENT, could shuffle them up (right now personal always at end)
    if (personal==True):
        #will also have to take it out so it can't be used again
        p=random.randint(0, len(personal_info)-1)
        b.append(str("Personal: "+personal_info[p]))
        personal_info.pop(p) #removing element from list
    else:
       while (picked==False):
        #pick a random number, make sure it hasn't been picked yet
            n=random.randint(0, len(info)-1)
            if (info[n] in b):
                picked=False
            else:
                b.append(info[n]) #put the value into the list
                picked==True
                break
    #random shuffling of the list
    random.shuffle(b)

    return b
                
#function to import data from a file
    #txt file for now
    #puts it into an array (each line)
    #will call in main one for personal and one for general 
def fromFile():
    stuff=[] #initialise array
    filename= input("Enter in the txt file name")
    fhandle = open (filename+".txt", 'r')
    for line in fhandle:
        line.rstrip() 
        stuff.append(str(line)) #adding stuff to array from txt file line

    fhandle.close()
    
    return stuff

#function to import data from txt file if we already know what we want
def fromFileKnown(filename):
    stuff=[] #initialise array
    fhandle = open (filename+".txt", 'r')
    for line in fhandle:
        line.rstrip() 
        stuff.append(str(line)) #adding stuff to array from txt file line

    fhandle.close()
    return stuff

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
7  6  5
"""
def formatBingo(info, gridNum, title):
    root = Tk()
    height = width= gridNum+1
    index=0
    #TITLE
    
    t= Label(root, text=title+" \n")
    t.grid(row=1, column=1, columnspan=width, sticky = W+E)
    
    #Fill out grid
    for i in range(2, height+1): #Rows
        #(starting at 2nd to leave space for title
        for j in range(2, width+1): #Columns
            #counter characters until new line 
            b = Label(root, text=info[index]+" \n \n \n", borderwidth=3, relief="solid") #.grid(row=i)
            b.grid(row=i, column=j, sticky=W+E+N+S) #sticky aligns West (left) and East (right)
            index+=1
    mainloop()
    return 0

#main program %%%%%%%%%%%%%%%%%%%%%%%
def pandaBingoTest():
    print("Test") #test works, rnadomises and returns the things in text files 
    general= fromFileKnown("panda")
    personal= fromFileKnown("panda_personal")
    personalBool=True
    result=(randomise(16, general, personal, personalBool)) #this is a dictionary 
    formatBingo(result, 4, "PANDA BINGO")
    return 0

#main menu with commands
def menu():
    print("Time to play bingo")
    gridSize = int(input("how many squares (n x n) square number in bingo grid?")) 
    #IMPROVEMENT, make it so program can round up to nearest square number

    personal = bool (input ("Are there any personal squares? True of False") )
    info = str(input ("Name of the file with the bingo square info: "))
    info_file = fromFileKnown(info) 
    if (personal==True):
        personal_info= fromFileKnown( input ("Name of the file with the personal info") )
    else:
        personal_info=""
    result = randomise(gridSize, info_file, personal_info, personal)
    title = input ("What's the title of the board?")
    formatBingo(result, int (math.sqrt(gridSize)), title)
    return 0

##%%%%%%%%%ACTUAL TEST%%%%%%%%%%%
#call this function to do a test with the values alread entered 
pandaBingoTest()

#This test is SCALABLE, you could do it with any bingo board 
menu()
