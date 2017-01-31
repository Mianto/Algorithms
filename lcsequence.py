 # naive Approch
def lcs(A, B, i, j):
	if i == 0 or j == 0:
		return 0
	if A[i-1] == B[j-1]:
		return 1 + lcs(A, B, i-1, j-1)
	else:
		return max(lcs(A, B, i-1, j), lcs(A, B, i, j-1))


# tabulation 
def lcs_tabulation(A, B):
	m = len(A)
	n = len(B)
	C = [[None]*(n+1) for i in xrange(m+1)]
	for i in range(m+1):
		for j in xrange(n+1):
			if i==0 or j == 0:
				C[i][j] = 0
			elif A[i-1] == B[j-1]:
				C[i][j] = C[i-1][j-1] + 1
			else:
				C[i][j] = max(C[i-1][j], C[i][j-1])
	return C[m][n]


# to get the sequence
def lcs_sequence(A, B):
	m = len(A)
	n = len(B)
	C = [[None]*(n+1) for i in xrange(m+1)]

	for i in xrange(m+1):
		for j in xrange(n+1):
			if i == 0 or j == 0:
				C[i][j] = 0
			elif A[i-1] == B[j-1]:
				C[i][j] = C[i-1][j-1] + 1 
			else:
				C[i][j] = max(C[i][j-1], C[i-1][j])
	print C[m][n]
	index = C[m][n]

	lcs_string = ['']*(index+1)
	lcs_string[index] = '\0'

	i = m
	j = n
	while i>0 and j>0:
		if A[i-1] == B[j-1]:
			lcs_string[index-1] = A[i-1]
			i -= 1
			j -= 1
			index -= 1
			
		elif C[i-1][j] > C[i][j-1]:
			i -= 1
		else:
			j -= 1
	return ''.join(lcs_string)


def main():
	X = "AGGTAB"
	Y = "GXTXAYB"
	
	# print lcs(X, Y, len(X), len(Y))
	# print lcs_tabulation(X, Y)
	print lcs_sequence(X, Y)

if __name__ == '__main__':
	main()