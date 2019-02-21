class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        if sum(nums) == 0: return '0'

        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        nums = nums[::-1]

        return str(''.join(str(num) for num in nums))



def compare(num1, num2):
    add1 = int(str(num1) + str(num2))
    add2 = int(str(num2) + str(num1))
    if add1 < add2:
        return False
    else:
        return True
