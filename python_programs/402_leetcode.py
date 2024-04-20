def removeKdigits(s: str, k: int) -> str:
    md = -1
    mdi = 0
    while k > 0:
        for i, d in enumerate(s):
            if int(d) > md:
                md = int(d)
                mdi = i
        print(s, s[i])
        s = s[:mdi] + s[mdi + 1:]
        print(s)
        k -= 1
        md = -1
        mdi = 0
    return s


if __name__ == '__main__':
    res = removeKdigits('1432219', 3)
    print(res)
