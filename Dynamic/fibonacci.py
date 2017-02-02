# bottom-up
def fibo(n):
	arr = [0]*(n+1)
	arr[1] = 1
	for i in xrange(2, n+1):
		arr[i] = arr[i-1]+arr[i-2]

	return arr[n]

# Top Down
def fibonacci(n, arr):
	if n == 0 or n == 1:
		arr[n] = n
	
	if arr[n] is None:
		arr[n] = fibonacci(n-1, arr)+fibonacci(n-2, arr)

	return arr[n]

def main():
	'''n = int(raw_input())
	print "Fibonacci of the Given Number", fibo(n)'''

	arr = [None]*100
	print "Fibonacci  of The Given Number", fibonacci(n, arr)

if __name__ == '__main__':
	main()
