class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = max_count = 0

        for i in nums:
            if i-1 not in nums_set:
                count = 1
                x = i
                while True:
                    if x+1 in nums_set:
                        count += 1
                        x += 1
                        continue
                    else:
                        max_count = max(max_count, count)
                        break

        return max_count
