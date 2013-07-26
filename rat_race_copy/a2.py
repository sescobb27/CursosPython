# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self,symbol,row,col,num_sprouts_eaten = 0):
        """
    	    (Rat, str, int, int) -> NoneType
    	"""
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self,row,col):
        """
    	    (Rat, int, int) -> NoneType
    	"""
        self.row = row
        self.col = col

    def eat_sprout(self):
        """
    	    (Rat) -> NoneType
    	"""
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
    	    (Rat) -> str
    	    symbol at (row, col) ate num_sprouts_eaten sprouts.
    	"""
        return "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol,self.row,self.col,self.num_sprouts_eaten)

    # Write your Rat methods here.

class Maze:
    """ A 2D maze. """
    def __init__(self,maze,rat_1,rat_2,num_sprouts_left = 3):
        """
    	    (Maze, list of list of str, Rat, Rat) -> NoneType
    	"""
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self,row,col):
        return self.maze[row][col] == WALL

    def get_character(self,row,col):
        if row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        elif row == self.rat_2.row and col == self.rat_2.col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self,rat,vertical_direction,horizontal_direction):
        row = rat.row
        col = rat.col
        height = len(self.maze)
        width = len(self.maze[0])
        if vertical_direction == UP and row + UP >= 0:
            char = self.maze[row + UP][col]
            if char == SPROUT:
                rat.eat_sprout()
                rat.set_location(row + UP,col)
                self.maze[row + UP][col] = HALL
                self.num_sprouts_left -= 1
                return True
            elif char == HALL:
                rat.set_location(row + UP,col)
                return True
            elif char == WALL:
                return False
        elif vertical_direction == DOWN and row + DOWN <= height:
            char = self.maze[row + DOWN][col]
            if char == SPROUT:
                rat.eat_sprout()
                rat.set_location(row + DOWN,col)
                self.maze[row + DOWN][col] = HALL
                self.num_sprouts_left -= 1
                return True
            elif char == HALL:
                rat.set_location(row + DOWN,col)
                return True
            elif char == WALL:
                return False
        elif horizontal_direction == LEFT and col + LEFT >= 0:
            char = self.maze[row][col + LEFT]
            if char == SPROUT:
                rat.eat_sprout()
                rat.set_location(row,col + LEFT)
                self.maze[row][col + LEFT] = HALL
                self.num_sprouts_left -= 1
                return True
            elif char == HALL:
                rat.set_location(row,col + LEFT)
                return True
            elif char == WALL:
                return False
        elif horizontal_direction == RIGHT and col + RIGHT <= width:
            char = self.maze[row][col + RIGHT]
            if char == SPROUT:
                rat.eat_sprout()
                rat.set_location(row,col + RIGHT)
                self.maze[row][col + RIGHT] = HALL
                self.num_sprouts_left -= 1
                return True
            elif char == HALL:
                rat.set_location(row,col + RIGHT)
                return True
            elif char == WALL:
                return False

    def __str__(self):
        temp = ""
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.rat_1.row == row and self.rat_1.col == col:
                    temp += self.rat_1.symbol
                elif self.rat_2.row == row and self.rat_2.col == col:
                    temp += self.rat_2.symbol
                else:
                    temp += self.maze[row][col]
            temp += "\n"
        temp += str(self.rat_1)+"\n"
        temp += str(self.rat_2)
        return temp

    # Write your Maze methods here.