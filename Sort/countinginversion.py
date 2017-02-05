def count_inversion(A, low, high):
    inv_count = 0
    if high > low:
        mid = (low + high) / 2
        inv_count = count_inversion(A, low, mid)
        inv_count += count_inversion(A, mid + 1, high)
        inv_count += merge_inversion(A, low, mid, high)
    return inv_count


def merge_inversion(A, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    # initialise temp list
    left = [0] * n1
    right = [0] * n2
    # copy value from original list
    for i in range(0, n1):
        left[i] = A[low + i]

    for i in range(0, n2):
        right[i] = A[mid + 1 + i]

    i = 0  # index of left list
    j = 0  # index of right list
    k = low  # index of original list
    count = 0
    while i < n1 and j < n2:
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            count += (n1 - i)
        k += 1
    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1

    return count


def main():
    A = [5, 1, 2, 3, 7, 8, 6, 4]
    n = len(A)
    print "Original Array"
    for i in range(n):
        print("%d " % A[i]),
    print '\n'
    inversion = count_inversion(A, 0, n - 1)
    print inversion


if __name__ == "__main__":
    main()
