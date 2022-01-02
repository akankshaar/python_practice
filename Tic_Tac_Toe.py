# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:49:40 2019

@author: Rhea Arora
"""
# -- Global Variables --
Board = [ "-","-","-",
          "-","-","-",
          "-","-","-",]

#if game still going
game_is_still_going = True

#who won?
winner= None

#who's turn is it?
current_player = "X"

def display_board():
    print (Board[0] + "|" + Board[1] + "|" + Board[2])
    print (Board[3] + "|" + Board[4] + "|" + Board[5])
    print (Board[6] + "|" + Board[7] + "|" + Board[8])
    
display_board()

def play_game():
    
    #display initial board
    display_board()
    
    while game_is_still_going:
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
    #The game has ended
    if winner == 0 or winner == X:
        print(winner + "won")
    elif winner == None:
        print("Tie")
        
        
        
def handle_turn(player):
    position = int(input("Choose a position from 0 to 9 : "))
    position = position - 1
    
    board[position] = "X"
    display_board()
    
def check_if_game_over():
    check_if_win()
    check_if_tie()
    
def check_if_win():
    #check rows
    #check columns
    #check diagonals
    return
    
def check_if_tie():
    return
    
play_game()