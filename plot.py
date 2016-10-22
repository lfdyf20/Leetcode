from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np



X = [0.1, 0.2, 0.4, 0.6, 0.8, 1]
# X = [0]*6 + [0.2]*6 + [0.4]*6 + [0.6]*6 + [0.8]*6 + [1]*6
X = np.array( X )

# Y = [1, 4, 7, 10, 13, 15]*6
Y = [1, 4, 7, 10, 13, 15]
Y = np.array( Y )

print(X)
print(Y)

Z = [ 
	85.5783, 85.6704, 85.6456, 85.2835, 85.146, 85.1668,
	85.5967, 85.7564, 85.4186, 85.394, 85.2773, 85.2159,
	85.4861, 85.4984, 85.2036, 85.136, 85.0255, 84.9518,
	85.4002, 85.2405, 84.9088, 84.9026, 84.6938, 84.7184,
	85.1115, 84.9825, 84.7368, 84.614, 84.4727, 83.5341,
	85.0071, 84.8719, 84.5648, 84.4051, 84.2516, 84.2393
]
Z = [ 
	[ 85.5783, 85.6704, 85.6456, 85.2835, 85.146, 85.1668],
	[ 85.5967, 85.7564, 85.4186, 85.394, 85.2773, 85.2159],
	[ 85.4861, 85.4984, 85.2036, 85.136, 85.0255, 84.9518],
	[ 85.4002, 85.2405, 84.9088, 84.9026, 84.6938, 84.7184],
	[ 85.1115, 84.9825, 84.7368, 84.614, 84.4727, 83.5341],
	[ 85.0071, 84.8719, 84.5648, 84.4051, 84.2516, 84.2393]
]
Z = np.array(Z)
print(Z)

# print("len(x)==len(y): ", len(x)==len(y))
print( 'len(x) == len(y) == len(z): ', len(X) == len(Y) == len(Z) )


print( "-"*15 )




def plot2D( X, Y, xLabel, yLable, title):
	plt.plot( X, Y )
	plt.xlabel(xLabel)
	plt.ylabel(yLable)
	plt.title(title)
	plt.show()

def plot3D(X, Y, Z, xLabel, yLable, zLabel, title):
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.set_zlabel( zLabel )
	X, Y = np.meshgrid(X, Y)
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=1, antialiased=False)
	# ax.set_zlim(-1.01, 1.01)
	# ax.zaxis.set_major_locator(LinearLocator(10))
	# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
	# ax.plot_wireframe(X, Y, Z)
	# surf.xlabel(xLabel)
	plt.xlabel(xLabel)
	plt.ylabel(yLable)
	plt.title(title)
	fig.colorbar(surf)
	plt.show()


xLabel = "k"
yLable = "Average Accuracy"
title = "K-NN"
# plot2D( x, y, xLabel, yLable, title )


plot3D( X, Y, Z, "Bag Size", "Number of Feature", "Average Accuracy", "Random Forest" )



