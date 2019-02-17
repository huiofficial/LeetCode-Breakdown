class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        left = self.findLeft(nums, target)
        if left == -1: return [-1, -1]

        return [left, self.findRight(nums, target)]

    def findLeft(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l, r = 0, len(nums)
        flag = -1
        while l < r:
            m = (l + r) // 2
            if target == nums[m]: flag = m

            if target > nums[m]: l = m +1
            else: r = m
        return flag

    def findRight(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l, r = 0, len(nums)
        flag = -1
        while l < r:
            m = (l + r) // 2
            if target == nums[m]: flag = m

            if target < nums[m]: r = m
            else: l = m + 1
        return flag
