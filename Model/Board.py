class Board:
  #Initialize the board class
  def __init__(self):
    self.__set_block_type()
    self.__set_animal_position()

  #Set the type of block, be it land, river, trap or den
  def __set_block_type(self):  

  #Set the position of the animal on the board
  def __set_animal_position(self):

  #Provide the type of block it is
  def give_block_information(self):
    return self.block_Type
    
  #After setting the blocks types and animal positions, the block information like isEmpty will be updated
  def update_block_information(self):
