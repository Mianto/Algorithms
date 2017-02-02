'''
Number of operation needed to perform to convert one string to 
another string.
Operations:
1)Insert
2)Remove
3)Replace

'''

def editDist(s1, s2):
	m, n = len(s1), len(s2)
	C = [[0]*(n+1) for x in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):

			if i == 0:
				C[i][j] = j

			if j == 0:
				C[i][j] = i

			elif s1[i-1] == s2[j-1]:
				C[i][j] = C[i-1][j-1]

			else:
				C[i][j] = 1 + min(C[i][j-1], C[i-1][j], C[i-1][j-1]) 
						
	return C[m][n]


def main():
	s1 = "saturday"
	s2 = "sunday"
	print editDist(s1, s2)


if __name__ == '__main__':
	main()