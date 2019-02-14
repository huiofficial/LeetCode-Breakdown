class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        i, j = 0, len(height) -1
        volume = 0
        while i < j:

            volume = max(volume, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]: i += 1
            else: j -= 1

        return volume
