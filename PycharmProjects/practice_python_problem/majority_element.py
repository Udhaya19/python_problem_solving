def majority_element(nums):
    # n = len(nums)
    # count = 0
    # for i in range(0, n):
    #     for j in range(i + 1, n):
    #         if nums[j] == nums[i]:
    #             count = count + 1
    #     if count >= n // 2:
    #         return nums[i]
    # return -1
    nums.sort()
    return nums[len(nums) // 2]


nums = [3, 1, 3]
print(majority_element(nums))
