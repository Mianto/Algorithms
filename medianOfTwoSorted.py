def median(A, n):
    if n%2 == 0:
        return A[n/2]
    else:
        return (A[n/2]+A[n/2+1])/2


def get_median(Array1, Array2, n):
    if n == 0:
        return -1
    if n == 1:
        return A[0]
    if n == 2:
        return (maxi(Array1[0],Array2[0])+mini(Array1[1],Array2[1]))/2
    m1 = median(Array1, n)
    m2 = median(Array2, n)

    if m1 == m2:
        return m1
    elif m1>m2:
        if n%2 == 0:
            return get_median(Array2[n/2-1: ], Array1, n-n/2+1)
        else:
            return get_median(Array2[n/2: ], Array1, n-n/2)
    else:
        if n%2 == 0:
            return get_median(Array1[n/2-1:], Array2, n-n/2+1)
        else:
            return get_median(Array1[n/2:], Array2, n-n/2)

def maxi(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def mini(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def main():
    A = [1, 12, 15, 26, 38]
    B = [2, 13, 17, 30, 45]

    print get_median(A, B, len(A)-1)

if __name__=="__main__":
    main()
