def isHappy(n: int) -> bool:

    visited = set()
    

    while n not in visited:
        print(f"1 N = {n}, visited : {visited}")

        visited.add(n)

        print(f"2 N = {n}, visited : {visited}")

        sum_d = 0

        while n:

            ld = n % 10
            sum_d += ld ** 2
            n = n // 10

            print(f"3 N = {n}, visited : {visited}, sum of digits : {sum_d}, last digit : {ld}")

        if sum_d == 1:
            return True
        else:
            n = sum_d

    print(f"4 N = {n}, visited : {visited}, sum of digits : {sum_d}")

    return False


if __name__ == '__main__':
    
    res = isHappy(19)
    
    print(res)