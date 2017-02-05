def merge_sort(A,low_index,high_index):
    if high_index > low_index :
        middle = (low_index + (high_index-1))/2
        merge_sort(A,low_index,middle)
        merge_sort(A,middle+1,high_index)
        merge_parts(A,low_index,middle,high_index)

def merge_parts(A,low,mid,high):
    n1 = mid - low + 1
    n2 = high - mid
    #initialise temp list
    left = [0]*n1
    right = [0]*n2
    #copy value from original list
    for i in range (0 , n1):
        left [i] = A[low+i]

    for i in range(0 , n2):
        right[i] = A[mid+1+i]

    i = 0 # index of left list
    j = 0 # index of right list
    k = low # index of original List

    while i < n1 and  j < n2:
        if left[i] <= right [j]:
            A[k] = left[i]
            i += 1
        else :
            A[k] = right[j]
            j += 1
        k += 1

    #copy the remaining pert of the left
    while i < n1 :
        A[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1

def main():
    A = list()
    n = int(raw_input("Enter Number of Elements : "))
    for i in range(n):
         x = int(raw_input())
         A.append(x)

    print "*******Unsorted Array*******"
    for i in range(n):
        print("%d " %A[i]),
    merge_sort(A,0,n-1)
    print '\n*****Sorted Array*********'
    for i in range(n):
        print("%d "%A[i]),

if __name__ == '__main__':
    main()
