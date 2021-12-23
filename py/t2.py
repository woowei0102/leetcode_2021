import math

def solution(A, B):
    x = int(math.sqrt(A))
    res = 0
    while (x <= B):
        if (x * (x + 1) >= A) and (x * (x + 1) <= B):
            res += 1
            x += 1
        else:
            return res
    

if __name__ == '__main__':
    print(solution(6, 20))