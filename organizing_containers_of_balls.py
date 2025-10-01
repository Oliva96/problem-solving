
#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#


def organizingContainers(container):
    d = {}
    n = len(container)
    for r in range(n):
        cap = sum([container[r][c] for c in range(n)])
        if cap in d: 
            d[cap] += 1 
        else:
            d[cap] = 1
    
    ans = True
    for c in range(n):
        cap = sum([container[r][c] for r in range(n)])
        if cap in d: 
            d[cap] -= 1 
        else:
            ans = False
    
    for v in d.values():
        if v != 0:
            ans = False
        
    return "Possible" if ans else "Impossible"

if __name__ == '__main__':
    
    container = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]

    print(organizingContainers(container))