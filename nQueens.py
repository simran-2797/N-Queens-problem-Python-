#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 11:27:10 2018

@author: simranmhatre
"""

def placeValid(row,col):
    for i in range(col):
        if(chessTable[row][i] == 1):
            return False
    i = row
    j = col
    while i>=0 and j >=0:
        if(chessTable[i][j] == 1):
            return False
        i = i -1
        j = j -1
        
    i = row
    j = col
    while i<numofQueens and j >=0:
        if(chessTable[i][j] == 1):
            return False
        i = i + 1
        j = j -1
    
    return True


def setQueens(col):
    if(col == numofQueens):
        return True
    for row in range(numofQueens):
        if(placeValid(row,col)):
            chessTable[row][col] = 1
            if(setQueens(col+1)):
                return True
            """Backtrack!"""
            chessTable[row][col] = 0
    return False


    
            
def printQueens():
    for i in range(len(chessTable)):
        for j in range(len(chessTable)):
            if(chessTable[i][j] == 1):
                print(" Q ",end=" ")
            else:
                print(" - ",end=" ")
        print()
                
        
def solve():
    if(setQueens(0)):
        printQueens()
    else:
        print("There is no solution....")

def main():
    solve()


numofQueens =int(input("Enter number of Queens"))
chessTable = list()
for i in range(numofQueens):
    small_array = list()
    for j in range(numofQueens):
        small_array.append(0)                
    chessTable.append(small_array)
main()    



