def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    matrix = [[0]*len(A) for i in range(len(B))]
    
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                matrix[j][i] = 1
    print(matrix)
a = [0,1,1,1,1]
b = [1,0,1,0,1]
A = [1,2,3,2,1]
B = [3,2,1,4,7]
findLength(A, B)


"""
[
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]
"""
















