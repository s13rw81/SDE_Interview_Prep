def sod(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

if __name__ == '__main__':
    res = sod(4415)
    print(res)

Python3 | Runtime 46ms Beats 89.09% ⭐ | Memory 16.57 MB Beats 41.03% ⭐ | Naive Approach