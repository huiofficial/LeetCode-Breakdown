class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        flag = nums[0]
        for i in range(len(nums)):
            if flag > nums[i]:
                return nums[i]

        return flag
