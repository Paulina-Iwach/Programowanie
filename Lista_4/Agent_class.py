import random


class Agent:
    """
    Class creates agent with initial location (x, y) and allows to change this location.
    """

    def __init__(self, x=random.randint(1, 60), y=random.randint(1, 60)):
        """
        Function creates agent with given (x,y) or random location.
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def move(self, x, y):
        """
        Function allows to move the agent by the given vector (x and y coordinates).
        :param x: x coordinate of the vector
        :param y: y coordinate of the vector
        :return: Agent's position after moving.
        """
        self.x += x
        self.y += y
        return self.x, self.y

