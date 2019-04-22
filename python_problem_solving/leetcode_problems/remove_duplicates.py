# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        value=len(nums)-1
        while value>0:
            if nums[value]==nums[value-1]:
                nums.pop(value)
            value-=1
        return len(nums)