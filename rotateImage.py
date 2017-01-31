import numpy as np

def rotate_image(Matrix, m, n):
	# ret_matrix = [[0 for i in xrange(n)] for i in xrange(m)]
	ret_matrix = np.zeros((n, m), dtype = np.int64)
	for i in xrange(m):
		for j in xrange(n):
			ret_matrix[j][m-i-1] = Matrix[i][j]

	return ret_matrix

def print_matrix(A, m, n):
	for i in range(m):
		for j in range(n):
			print A[i][j],
		print '\n'

def main():
	A = np.arange(12).reshape(3,4)
	print_matrix(A, 3, 4)

	print "===Rotate-Matrix===="

	B = rotate_image(A, 3 ,4)
	print_matrix(B, 4, 3)
	

if __name__=="__main__":
	main()



