class SnakeBodyUnit(object):

    def __init__(self, pos):
        self.pos = pos
        self.next = None
        self.pre = None


class Snake(object):

    def __init__(self, head):
        snakeHead = SnakeBodyUnit(head)
        self.head = snakeHead
        self.tail = snakeHead

    def moveHead(self, pos):
        """[summary]
        move head to pos
        [description]
        move the snake's head to the new position
        Arguments:
            pos {tuple(int, int)} -- a position on the map
        """
        newHead = SnakeBodyUnit(pos)
        newHead.next, self.head.pre = self.head, newHead
        self.head = newHead

    def removeTail(self):
        """
        remove the tail
        """
        self.tail = self.tail.pre
        self.tail.next = None


class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.height, self.width = height, width
        self.foodpos = food[::-1]
        self.snake = Snake((0,0))
        self.bodyZone = {(0,0)}
        self.score = 0
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.snake.head.pos
        if direction == "U":
            x -= 1
        elif direction == "D":
            x += 1
        elif direction == "L":
            y -= 1
        else:
            y += 1
        newPos = (x, y)
        self.bodyZone.remove(self.snake.tail.pos)
        if 0 <= x < self.height and 0 <= y < self.width and newPos not in self.bodyZone:
            self.bodyZone.add(newPos)
            self.snake.moveHead(newPos)
            if self.foodpos and newPos == tuple(self.foodpos[-1]):
                self.score += 1
                self.foodpos.pop()
                self.bodyZone.add(self.snake.tail.pos)
            else:
                self.snake.removeTail()            
        else:
            self.score = -1
        return self.score



        


# Your SnakeGame object will be instantiated and called as such:
width = 3
height = 3
food = [[2,0],[0,0],[0,2],[2,2]]


obj = SnakeGame(width, height, food)

for direction in "DDRUULDRRULD":
    score = obj.move(direction)
    # print( obj.bodyZone )
    # print("snake: ", obj.snake.head.pos, obj.snake.tail.pos)
    print(score)