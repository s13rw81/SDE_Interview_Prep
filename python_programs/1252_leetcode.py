from typing import List
def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    row = []
    for i in range(n):
        row.append(0)
    column = []
    for i in range(m):
        column.append(0)
    for index in indices:
        column[index[0]] += 1
        row[index[1]] += 1
    rowOdds = 0
    rowEvens = 0
    for i in row:
        if i % 2 != 0:
            rowOdds += 1
        else:
            rowEvens += 1
    total = 0
    for i in column:
        if i % 2 == 0:
            total += rowOdds
        else:
            total += n - rowOdds
    return total

#
#
# def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
#     # Creating a 2D array filled with zeros
#     array_2d = [[0 for j in range(n)] for i in range(m)]
#
#     for i in indices:
#         r = i[0]
#         c = i[1]
#         for x in range(m):
#             for y in range(n):
#                 if x == r:
#                     array_2d[x][y] += 1
#                 if y == c:
#                     array_2d[x][y] += 1
#
#     return array_2d
#
#
if __name__ == '__main__':
    res = oddCells(m=2, n=3, indices=[[0, 1], [1, 1]])
    print(res)

    res = oddCells(m=2, n=2, indices=[[1,1],[0,0]])
    print(res)
