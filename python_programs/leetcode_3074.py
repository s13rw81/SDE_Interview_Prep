from typing import List
def minimumBoxes(apple: List[int], capacity: List[int]) -> int:

    ta = sum(apple)
    lc = len(capacity)
    tc = sum(capacity)
    if tc == ta:
        return lc
    if tc < ta:
        return 0

    capacity = sorted(capacity, reverse=True)
    ctr = 0
    j = 1
    while j < lc:
        if sum(capacity[: j]) >= ta:
            return j
        else:
            j += 1
    return lc

if __name__ == '__main__':
    capacity = [4,3,1,5,2]
    apple = [1,3,2]
    res = minimumBoxes(apple, capacity)
    print(res, 'prob 1')

    capacity = [2,4,2,7]
    apple = [5,5,5]
    res = minimumBoxes(apple, capacity)
    print(res, 'prob 2')

    capacity = [5,5,5]
    apple = [5,5,5]
    res = minimumBoxes(apple, capacity)
    print(res, 'prob 3')

    capacity = [1, 7, 2]
    apple = [11]
    res = minimumBoxes(apple, capacity)
    print(res, 'prob 4')