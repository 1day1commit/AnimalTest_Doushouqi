class Animal:
    # Intialize the Animal Class
    def __init__(self, i: int, aliveState: bool, swimableState: bool, jumpableState: bool, x: int, y: int, team: str):
        # The ranking of the animal for capture comparison
        self.__rank = i
        # A boolean statement of whether the animal piece has been captured or not
        self.__alive = aliveState
        # A boolean statement of whether the animal can swim through the river tile, True for rat, False for the rest
        self.__swimable = swimableState
        # A boolean statement of whether the animal can jump over the river, True for lion and tiger, False for the rest
        self.__jumpable = jumpableState
        # The x and y coordinates of the animal on the board
        self.__position = [x, y]
        # The ownership of each individual piece
        self.__team = team

    # setting conditions to animals
    # for setting the animal's alive status to false if the animal gets captured
    def set_alive(self, aliveState: bool):
        self.alive = aliveState
    # selecting where the animal will move the board, using x and y coordinates

    def set_position(self, x, y):
        self.position = [x, y]

    # return the rank of the animal to other components for rank comparison
    def give_rank(self):
        return self.rank

    # return the position of the animal to other components(usually the board object)
    def give_position(self):
        return self.position

    # if any animal is trapped, set the animal to be eatable by all other opponent's pieces
    def vulnerable(self, i: int):
        self.rank = i

    # return to the status while not being trapped
    def not_vulnerable(self, i: int):
        self.rank = i

# Animal classes


class Elephant(Animal):
    def __init__(self, team: str):
        pass


class Lion(Animal):
    def __init__(self, team: str):
        pass


class Tiger(Animal):
    def __init__(self, team: str):
        pass


class Leopard(Animal):
    def __init__(self, team: str):
        pass


class Dog(Animal):
    def __init__(self, team: str):
        pass


class Cat(Animal):
    def __init__(self, team: str):
        pass


class Rat(Animal):
    def __init__(self, team: str):
        pass
