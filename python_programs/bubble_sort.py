def bubble_sort(arr: list[int]) -> list[int | None]:
	ln = len(arr)

	for i in range(ln):
		for j in range(ln - i - 1):
			if arr[j] > arr[j + 1]:
				temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = temp
			print(arr)
	return ['arr']

bubble_sort([1, 3, 2, 5, 0, 4, 11, 1, 1, 0])
