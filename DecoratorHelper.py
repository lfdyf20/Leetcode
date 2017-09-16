import time

def timer(func):
	def wrapper(*args, **kv):
		start = time.time()
		res = func( *args, **kv )
		runtime = time.time()-start
		print( "[{func} runtime]:\t {runtime}".format( 
			func=func.__name__,  runtime=runtime) )
		return res
	return wrapper


# Draw a Binary Tree
def drawTree(root):
	def height(root):
		return 1 + max(height(root.left), height(root.right)) if root else -1
	
	def jumpto(x, y):
		t.penup()
		t.goto(x, y)
		t.pendown()
	
	def draw(node, x, y, dx):
		if node:
			t.goto(x, y)
			jumpto(x, y-20)
			t.write(node.val, align='center', font=('Arial', 12, 'normal'))
			draw(node.left, x-dx, y-60, dx/2)
			jumpto(x, y-20)
			draw(node.right, x+dx, y-60, dx/2)
	
	import turtle
	t = turtle.Turtle()
	t.speed(0); turtle.delay(0)
	h = height(root)
	jumpto(0, 30*h)
	draw(root, 0, 30*h, 40*h)
	t.hideturtle()
	turtle.mainloop()



def drawBinaryTree(func):
	def wrapper(*args, **kv):
		root = func(*args, **kv)
		drawTree(root)
		return root
	return wrapper


		