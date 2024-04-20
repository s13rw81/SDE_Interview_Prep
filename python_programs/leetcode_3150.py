from typing import List


def longestMonotonicSubarray(nums: List[int]) -> int:
    inc_l = 0
    dec_l = 0
    inc = list()
    dec = list()

    for i in nums:
        if inc:
            if inc[-1] >= i:
                inc.clear()
                inc.append(i)
            else:
                inc.append(i)
        else:
            inc.append(i)
        inc_l = max(inc_l, len(inc))

        if dec:
            if dec[-1] <= i:
                dec.clear()
                dec.append(i)
            else:
                dec.append(i)
        else:
            dec.append(i)
        dec_l = max(dec_l, len(dec))

    return max(inc_l, dec_l)


if __name__ == '__main__':
    r = longestMonotonicSubarray([1,4,3,3,2])
    print(r)
    r = longestMonotonicSubarray([3,3,3,3])
    print(r)
    r = longestMonotonicSubarray([3,2,1])
    print(r)
    r = longestMonotonicSubarray([1, 1, 5])
    print(r)
    r = longestMonotonicSubarray([6, 6, 3])
    print(r)

