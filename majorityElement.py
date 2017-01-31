def binary_search(A,low,high,x):
    if high >= low:
        mid = (high + low )/2
        if (mid == 0 or A[mid-1]<x) and x == A[mid]:#checking first occurence of x
            return mid
        elif x > A[mid]:
            return binary_search(A,mid+1,high,x)
        else:
            return binary_search(A,low,mid-1,x)
    else:
        return -1

def is_majority(A,n,x):
    i = binary_search(A,0,n-1,x)
    if i == -1:
        return False
    if (i+n/2 <= n-1) and A[i+n/2] == x:
        return True
    else:
        return False

def main():
    A = [1, 2, 3, 3, 3, 3, 10]
    print is_majority(A,len(A),3)

if __name__ == '__main__':main()
