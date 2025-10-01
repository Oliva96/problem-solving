
directions = [(0,-1), (0,1), (1,0), (-1,0), (-1,-1), (1,-1), (1,1), (-1,1)]

def queensAttack(n, k, r_q, c_q, obstacles):
    obs = set()
    for r, c in obstacles:
        obs.add((r, c))

    def valid_pos(rq, cq):
        if rq > n or cq > n or rq < 1 or cq < 1:
            return False
        if (rq, cq) in obs:
            return False
        return True
    
    ans = 0
    for r, c in directions:
        rq = r_q + r
        cq = c_q + c
        while(valid_pos(rq, cq)):
            ans += 1
            rq += r
            cq += c
    
    return ans

if __name__ == '__main__':

    n = 1
    k = 0
    r_q = 1
    c_q = 1
    obstacles = [[5, 5], [4, 2], [2, 3]]

    # obstacles = []
    print(queensAttack(n, k, r_q, c_q, obstacles))
