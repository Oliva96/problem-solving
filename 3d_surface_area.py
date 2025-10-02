
import os

def surfaceArea(A):
    r = len(A)
    c = len(A[0])
    ans = 2*r*c
    ans += sum(A[0])
    ans += sum(A[r-1])
    ans += sum(A[i][0] for i in range(r))
    ans += sum(A[i][c-1] for i in range(r))

    for i in range(r-1):
        for j in range(c):
            ans += abs(A[i][j] - A[i+1][j])
    
    for i in range(c-1):
        for j in range(r):
            ans += abs(A[j][i] - A[j][i+1])
    
    return ans
    

if __name__ == '__main__':
    A = [[1]]

    print(surfaceArea(A))
