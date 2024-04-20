# max area between 2 lines

def findMaxArea(array: list):
	la = len(array)
	if la < 2:
		return None
	p1 = 0
	p2 = la - 1
	ma = 0
	while p1 < p2:
		mat = min(array[p1], array[p2]) * (p2 - p1)
		ma = max(ma, mat)
