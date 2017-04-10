def lis(a):
    n = len(a)
    li = [1] * n

    for i in xrange(1, n):
        for j in xrange(0, i):
            if a[i] > a[j] and li[i] < li[j] + 1:
                li[i] = li[j] + 1

    return max(li)
arr = [3, 7, 2, 40, 80]
print lis(arr)
