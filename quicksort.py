from random import randrange


def quick_sort(A, low, high):
    if high > low:
        pivot_index = randrange(low, high+1)
        pivot = partition(A, low, high, pivot_index)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)


def partition(A, low, high, pivot):
    A[pivot], A[high] = A[high], A[pivot]
    store_index = low
    for j in xrange(store_index, high):
        if A[j] < A[high]:
            A[store_index], A[j] = A[j], A[store_index]
            store_index += 1
    A[store_index], A[high] = A[high], A[store_index]
    return store_index


def main():
    A = [2,7,1,23,89,12,16,11,12]
    quick_sort(A,0,len(A)-1)

    print A

if __name__=="__main__":main()
