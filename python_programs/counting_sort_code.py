def counting_sort(nums: list[int]) -> list[int]:
	ln = len(nums)
	# find range of the array
	high = max(nums)
	low = min(nums)
	counts = [0] * high
	for n in nums:
		count[n] += 1
	# expand the array
	result = [0] * ln

	for i, n in enumerate(counts):
		