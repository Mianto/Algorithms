import random
import quicksort


def RSelection(A, low, n, order_statistic):
    if low == n:
        return A[low]
    if order_statistic == 0:
        return -1
    if n > low:
        pivot = random.randrange(low, n+1)
        pivot_index = quicksort.partition(A, 0, n, pivot)
        i = pivot_index-low+1
        if i == order_statistic:
            return A[pivot_index]
        elif i > order_statistic:
            return RSelection(A, low, pivot_index-1, order_statistic)
        else:
            return RSelection(A, pivot_index+1, n, order_statistic-i)


def main():
    A = [12, 3, 5, 7, 4, 19, 26]
    order = int(raw_input("Enter Order :"))

    print RSelection(A, 0, len(A)-1, order)
    quicksort.quick_sort(A,0,len(A)-1)
    print A
    print A[order+1]

if __name__=='__main__':main()
