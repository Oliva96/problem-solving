
import bisect

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    final_ranked = sorted(set([-i for i in ranked]))
    return [bisect.bisect_left(final_ranked, -i) + 1 for i in player]

if __name__ == '__main__':
    
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]
    print(climbingLeaderboard(ranked, player))
