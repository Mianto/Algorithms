def maxDiff(A):
	minimumElement = A[0]
	max_diff = abs(A[1]-A[0])
	for i in range(1, len(A)):
		if abs(A[i]-minimumElement) > max_diff:
			max_diff = abs(A[i]-minimumElement)
		if A[i] < minimumElement:
			minimumElement = A[i]
	return max_diff

def main():
	A = [2, 6, 9, 10, 1, 16, 3]
	print maxDiff(A)

if __name__ == '__main__':
    main()
