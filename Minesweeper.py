import collections
class Solution(object):
    def updateBoard(self, board, click):
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = collections.deque()
        queue.append((click[0], click[1]))
        valid_neighbours = lambda pos: 0<=pos[0]<m and 0<=pos[1]<n == True

        while queue:
            x, y = queue.pop()
            if board[x][y] == 'M':
                board[x][y] = 'X'
            else:
                # Filter out the valid neighbours
                neighbours = filter(valid_neighbours, [(x-1, y), (x+1, y), 
                    (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)])
                # Count the number of mines amongst the neighbours
                mine_count = sum([board[i][j]=='M' for i, j in neighbours])
                # If at least one neighbour is a potential mine, store the mine count.
                if mine_count > 0:
                    board[x][y] = str(mine_count)
                # If no neighbour is a mine, then add all unvisited neighbours
                # to the queue for future processing
                else:
                    board[x][y] = 'B'
                    queue.extend([(i, j) for (i, j) in neighbours if board[i][j]=='E'])
        return board



board = ["EEEEE","EEMEE","EEEEE","EEEEE"]
click = [3,0]

sl = Solution()
print( sl.updateBoard( board, click ) )