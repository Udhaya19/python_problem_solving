def array_rotation(nums, k):
    # num1 = nums[:k]
    # num = len(nums)
    k = abs(k % len(nums))

    nums[k:], nums[: k] = nums[:len(nums) - k], nums[len(nums) - k:]
    print(nums)


nums = [1, 2]
k = 3
array_rotation(nums, k)
