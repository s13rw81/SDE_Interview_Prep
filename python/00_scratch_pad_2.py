def sod(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

if __name__ == '__main__':
    res = sod(4415)
    print(res)