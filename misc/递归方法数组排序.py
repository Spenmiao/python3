
nums = [3, 2, 4, 5, 1, 9, 10, 6, 8, 7, 111]

def funsort(nums):
	l = []
	for i, j in enumerate(nums[1:]):
		if nums[0] > j:
			nums[0] , nums[i+1] = nums[i+1], nums[0]
	l.append(nums[0])
	# print(nums)
	if len(nums) == 2:
		return nums
	return l + funsort(nums[1:])
print(funsort(nums))
