class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        '''
        flag = nums[0]
        for i in range(len(nums)):
            if flag > nums[i]:
                return nums[i]

        return flag
        '''
        pos = self.findPosition(nums)
        if pos == len(nums): return nums[0]
        return nums[pos]

    def findPosition(self, nums: 'List[int]') -> 'int':
        flag = nums[0]
        l, r = 1, len(nums)
        while l < r:
            m = (l + r) // 2
            if flag < nums[m]: l = m + 1
            else: r = m

        return l
        
