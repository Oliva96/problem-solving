from collections import Counter

def makeAnagram(a, b):
    ca = Counter(a)
    cb = Counter(b)

    union = ca | cb
    intersection = ca & cb

    return sum(union.values()) - sum(intersection.values())

if __name__ == '__main__':

    a = 'cde'

    b = 'abcc'

    print(makeAnagram(a, b))