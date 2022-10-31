import unittest
from Model.Animal import *


class AnimalTest(unittest.TestCase):
    # test function to test equality of two value
    a = Animal(1, True, True, 1, 2, "a")

    def set_alive(self):
        self.assertEqual(self.aliveState, False)


if __name__ == '__main__':
    unittest.main()
