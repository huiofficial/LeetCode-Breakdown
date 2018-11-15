class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or len(nums) == 1: return len(nums)
        i = 1
        temp = nums[0]
        while True:
            if nums[i] == temp:
                del(nums[i])
                i -= 1
            else: temp = nums[i]

            if i >= len(nums)-1: break

            i += 1

            if i == 0: break

        return len(nums)
