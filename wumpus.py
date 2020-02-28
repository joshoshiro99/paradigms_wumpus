from random import seed
from random import randint
import time
import keyboard
import os

wumpyX = 0;
wumpyY = 0;
'''
     todo:
     1: random map generation
     2: AI for the wumpus
     3: grid display w/ fog of war
'''

def adjust_wumpus( w_adj, gold, wumpus ):
    if w_adj == 1:
        wumpus[0] = gold[0]-1
        wumpus[1] = gold[1]-1

    elif w_adj == 2:
        wumpus[0] = gold[0]-1
        wumpus[1] = gold[1]

    elif w_adj == 3:
        wumpus[0] = gold[0] +1
        wumpus[1]= gold[1]+1

    elif w_adj == 4:
        wumpus[0] = gold[0]
        wumpus[1] = gold[1]-1
        
    elif w_adj == 6:
        wumpus[0] = gold[0]
        wumpus[1] = gold[1]+1
    elif w_adj == 7:
        wumpus[0] = gold[0]+1
        wumpus[1] = gold[1]-1
    elif w_adj == 8:
        wumpus[0] = gold[0]+1
        wumpus[1] = gold[1]
    elif w_adj == 9:
        wumpus[0] = gold[0] +1
        wumpus[1] = gold[1] +1
    wumpyX = wumpus[0]
    wumpyY = wumpus[1]
    print (wumpus[0])
    print (wumpus[1])
    print (wumpyX)
    print (wumpyY)

    return;
def place_tile( board, coords, tile_name):
    x = coords[0]
    y = coords[1]
    board[x][y] = tile_name
    return;
def GenerateBoard(board):
    gold = [0,0]
    #place gold first
    gold[0] = randint(1,2) #from 1(incl) to 2(incl) causes gold to be generated within center region 
    gold[1] = randint(1,2)
    place_tile(board, gold, "GOLD")
    #place wumpus adj to gold
    #rand int from 1-9 corresponds to tile around gold
    #eg: 1 2 3
    #    4 G 6
    #    7 8 9
    wumpus = [0,0]
    w_adj = randint(1,10)
    if w_adj == 5:  #regen if on gold tile
        w_adj = randint(1,10)
    else:
        adjust_wumpus(w_adj, gold,wumpus) #adj wumpus coords
    place_tile(board, wumpus, "WUMPUS")

    #place 3 pits
    pits = [0,0]
    breeze = [0,0]

    pits[0] = randint(1,3)
    pits[1] = randint(0,3)
    place_tile(board, pits, "PIT")

	

    pits[0] = randint(1,3)
    pits[1] = randint(0,3)
    place_tile(board, pits, "PIT")
    pits[0] = randint(1,3)
    pits[1] = randint(0,3)
    place_tile(board, pits, "PIT")

    return;
def outputBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(" ", board[i][j], end = " ")
        print("\n")
    return;

board=[["SAFE","SAFE","SAFE","SAFE"],
        ["SAFE","SAFE","SAFE","SAFE"],
        ["SAFE","SAFE","SAFE","SAFE"],
        ["SAFE","SAFE","SAFE","SAFE"]]
row=0
column = randint(0,3)
arrow=True
game=True
score=0

player = [row, column]
GenerateBoard(board)
place_tile(board,player, "player")

while(game):
    
    #user is given prompt and moves
    #movement logic
    outputBoard(board)
    place_tile(board, player, "safe")
    
    choice=input("press w to move up\npress s to move down\npress a to move left\npress d to move right\n")
    if choice == "w":
        if row != 0: #not at top? go up one row
            row = row - 1
        else:
            print("move denied")        
    elif choice ==  "s" : #not at bottom row? go down one row
        if row!=3:
            row = row +1
        else:
            print("move denied")        
    elif choice ==  "a" : #not at far left corner? go left one col
        if column!=0:
            column = column -1
        else:
            print("move denied")
    elif choice ==  "d" : #not at far right? go right one col
        if column!=3:
            column = column + 1
        else:
            print("move denied")        
    else:
        print("move denied")
    player = [row,column]
    place_tile(board, player, "player")
    time.sleep(1)
    os.system("cls")

    #smell logic:
    
    if board[row][column]=="Smell" and arrow != False:
        yeet = input("do you want to throw an arrow-->\npress y to throw\npress n to save your arrow\n")
        if keyboard.read_key() == "y":
            yeet = input("press w to throw up\npress s to throw down\npress a to throw left\npress d to throw right\n")
            if yeet == "w":
                if board[row-1][column] == "WUMPUS":
                    print("wumpus killed!")
                    score+=1000
                    print("score: ",score)
                    board[row-1][column] = "Safe"
                    board[1][0]="Safe"
                    board[3][0]="Safe"
                else:
                    print("arrow wasted...")
                    score-=10
                    print("score: ",score)
            elif yeet == "s":
                if board[row+1][column] == "WUMPUS":
                    print("wumpus killed!")
                    score+=1000
                    print("score: ",score)
                    board[row+1][column] = "Safe"
                    board[1][0]="Safe"
                    board[3][0]="Safe"
                else:
                    print("arrow wasted...")
                    score-=10
                    print("score: ",score)
            elif yeet == "a":
                if board[row][column-1] == "WUMPUS":
                    print("wumpus killed!")
                    score+=1000
                    print("score: ",score)
                    board[row][column-1] = "Safe"
                    board[1][0]="Safe"
                    board[3][0]="Safe"
                else:
                    print("arrow wasted...")
                    score-=10
                    print("score: ",score)
            elif yeet == "d":
                if board[row][column+1] == "WUMPUS":
                    print("wumpus killed!")
                    score+=1000
                    print("score: ",score)
                    board[row][column+1] = "Safe"
                    board[1][0]="Safe"
                    board[3][0]="Safe"
                else:
                    print("arrow wasted...")
                    score-=10
                    print("score: ",score)
                
            
            arrow=False
    #endgame conditions:
    if board[row][column] == "WUMPUS" :
        score-=1000
        print("\nWumpus here!!\n You Die\nAnd your score is: ",score
              ,"\n")
        break
    if(board[row][column]=='GOLD'):
        score+=1000
        print("GOLD FOUND!You won....\nYour score is: ",score,"\n")
        break
    if(board[row][column]=='PIT'):
        score-=1000
        print("Ahhhhh!!!!\nYou fell in pit.\nAnd your score is: ",score,"\n")
        break
    

