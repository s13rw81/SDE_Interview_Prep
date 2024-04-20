def leftRightDifference(nums):
    len_nums = len(nums)
    left_sum = [0] * len_nums
    right_sum = [0] * len_nums
    answer = [0] * len_nums

    for i in range(len_nums):
        left_sum[i] = sum(nums[: i])
        right_sum[i] = sum(nums[i + 1 :])

    print(left_sum, right_sum)
if __name__ == '__main__':
	leftRightDifference([10, 4, 8, 3])