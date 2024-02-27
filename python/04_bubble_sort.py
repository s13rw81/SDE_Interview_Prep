def bubble_sort(a: list) -> list:
	if a == None:
		return
	print(a)
	len_a = len(a)
	for j in range(len_a -1, 0, -1):
		for i in range(j):
			if a[i] < a[i + 1]:
				temp = a[i + 1]
				a[i + 1] = a[i]
				a[i] = temp
			print(a)

if __name__ == '__main__':
	bubble_sort([2, 1, 4, 2, 9, 6, 7, 12, 1, 34, 562, 54, 77])

