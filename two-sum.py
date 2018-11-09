class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict: return [dict[target-num], i]
            else:
                dict[num] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)
