# class Solution(object):
#     def twoSum(self, nums, target):
#         """Brute force"""
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution(object):
    def twoSum(self, nums, target):
        nums_copy = nums[:]
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                nums_copy[i] = '-'
                return [i, nums_copy.index(target - nums[i])]
