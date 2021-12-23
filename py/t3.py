def solution(N, R, C):
    res = []
    # 初始化
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        res.append(temp)

    # 設炸彈
    for i in range(len(R)):
        res[R[i]][C[i]] = 'B'
    
    # 設數字
    for i in range(len(R)):
        # 上
        print(R[i], C[i])
        if (R[i] + 1) < N and res[R[i] + 1][C[i]] != 'B' :
            res[R[i] + 1][C[i]] += 1
        # 下
        if (R[i] - 1) >= 0 and res[R[i] - 1][C[i]] != 'B':
            res[R[i] - 1][C[i]] += 1
        # 左
        if (C[i] - 1) >= 0 and res[R[i]][C[i] - 1] != 'B':
            res[R[i]][C[i] - 1] += 1
        # 右
        if (C[i] + 1) < N and res[R[i]][C[i] + 1] != 'B':
            res[R[i]][C[i] + 1] += 1

        # 右上
        if (R[i] + 1) < N and (C[i] + 1) < N and res[R[i] + 1][C[i] + 1] != 'B' :
            res[R[i] + 1][C[i] + 1] += 1
        # 右下
        if (R[i] - 1) >= 0 and (C[i] + 1) < N and res[R[i] - 1][C[i] + 1] != 'B' :
            res[R[i] - 1][C[i] + 1] += 1
        # 左上
        if (R[i] + 1) < N and (C[i] - 1) >= 0 and res[R[i] + 1][C[i] - 1] != 'B' :
            res[R[i] + 1][C[i] - 1] += 1
        # 左下
        if (R[i] - 1) >= 0 and (C[i] - 1) >= 0 and res[R[i] - 1][C[i] - 1] != 'B' :
            res[R[i] - 1][C[i] - 1] += 1
    print(res)

if __name__ == '__main__':
    print(solution(3, [2, 1, 0, 2], [0, 2, 1, 2]))
