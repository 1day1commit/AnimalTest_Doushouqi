class Block:
  #Intialize the board tile types, conditions and positions of normal and special tiles classes
  def __init__(self, blockType:str, isEmpty:bool, position:[]):
    self.__blockType = blockType
    self.__isEmpty = isEmpty
    self.__position = position

  #return the information if the selected block is 'empty or not' to the 'GameController'
  def give_isEmpty(self):
    return self.isEmpty

  #return the information of where this block locates in the board
  def give_position(self):
    return self.position


    




      


    
  


    
  
  