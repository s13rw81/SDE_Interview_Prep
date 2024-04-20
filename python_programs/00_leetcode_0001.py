# two sum problem
def main(array: list, target: int):
    memo = dict()
    la = len(array)
    for i in range(la):
        part = target - array[i]
        if part in memo:
            return [memo[part], i]
        else:
            memo[array[i]] = i
    return []

if __name__ == '__main__':
    res = main(array=[1,3,7,9,2], target=16)
    print(res)