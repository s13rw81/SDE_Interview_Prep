# pascals triangle using dynamic programming
memo = dict()
def triangle(n=3):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] =  pascals(i - 1, j - 1) + pascals(i - 1, j)
    return result


def pascals(n, k):
    global memo
    if (k <= 0 or k == n):
        return 1
    else:
        if (n, k) in memo :
            return memo[ (n, k) ]
        else:
            memo[ (n, k) ] = (pascals(n - 1, k - 1) + pascals(n - 1, k))        
        return memo[ (n , k) ]


if __name__ == '__main__':

    res = triangle(20)
    print(res)