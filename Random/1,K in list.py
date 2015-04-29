def function(A,K):
    return set(range(1,K+1)).issubset(set(A))

print(function([1,2,5,2,3,4,3,6],6))

