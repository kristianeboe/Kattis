def isItSortable(A):
    n = len(A)
    counter = 0
    for i in range(n-1):
        print(i)
        if counter > 1:
            return False
        if A[i] > A[i+1]:
            counter += 1
            for j in range(i,n-2):
                if A[j] < A[i]:
                    i = j
                    break
    return True


A = [1,2,3,4,5]
print(isItSortable(A))

A = [1,3,2,4,5]
print(isItSortable(A))

A = [1,2,3,4,3,3,5]
print(isItSortable(A))

A = [5,4,3,2,1]
print(isItSortable(A))