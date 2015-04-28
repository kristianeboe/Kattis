def isItSortable(A):
    n = len(A)
    counter = 0
    i = 0
    while i < n - 1:
        print(i)
        if counter > 1:
            return False
        if A[i] > A[i + 1]:
            counter += 1
            for j in range(i, n - 2):
                if A[j] < A[i]:
                    i = j
                    i -= 1
                    break
        i += 1
    if counter > 1:
        return False
    return True


A = [2, 1, 3, 4, 5]
print(isItSortable(A))

A = [1, 1, 4, 3, 5, 9, 8]
print(isItSortable(A))