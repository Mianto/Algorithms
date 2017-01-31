def leftRotate(Array, n, d):
	for i in range(gcd(d, n)):
		temp = Array[i]
		j = i
		while(True):
			k = j + d
			if k >= n:
				k = k-n
			if k == i:
				break
			Array[j] = Array[k]
			j = k
		Array[j] = temp 

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

def main():
	A = [1, 2, 3, 4, 5]
	leftRotate(A, len(A), 4)
	for i in range(len(A)):
		print A[i],


if __name__=="__main__":
	main()
