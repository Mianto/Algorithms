import numpy as np


def rotate_anticlockwise(Matrix, N):
	for x in range(0, N/2):
		for y in range (x, N-x-1):
			temp = Matrix[x][y]
			# move values from right to top
			Matrix[x][y] = Matrix[y][N-1-x]
 
            # move values from bottom to right
			Matrix[y][N-1-x] = Matrix[N-1-x][N-1-y]
 
            # move values from left to bottom
			Matrix[N-1-x][N-1-y] = Matrix[N-1-y][x]
 
            # assign temp to left
			Matrix[N-1-y][x] = temp


def main():
	A = np.arange(16).reshape(4,4)
	print A

	for i in range(3):
		rotate_anticlockwise(A, 4)
	print A
if __name__ == '__main__':
	main()
