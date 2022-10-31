import Board.py
class GameController:
  #Initializes the class Board
  def __init__(self,board:Board)
  
  #Verification of user_input of which game function the user chose(save, continue, new game)
  def main_page_command_verification():
    return True #or False if it is invalid
  #Exits the game 
  def exit():

  #Starts a new game
  def new_game():

  #Load up the last saved game
  def continue_game():

  #Initialize the game board with board tiles and pieces
  def init_board()

  # Verification of in-game features such as move pieces
  def in_game_command_verification():
    return True #or False if it is invalid
  #save the existing game
  def save():

  #leave the current game being played
  def quit():

  #Select the individual pieces to move on the game board
  def move_selection():

  #Check whether the move can be done using several conditional statements
  def is_valid_move(player:int,animal_rank:int,x:int,y:int):
    return True #or False for invalid move

  #After selecting, moving , etc, the game will update the data with the latest user choices
  def update_gameData():
    
  #Check the game data to identify if someone wins
  def check_winning():#

  #Change the player's turn
  def changeTurn():





