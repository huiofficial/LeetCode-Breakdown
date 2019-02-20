class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        if len(nums) < 3: return False

        one = two = None

        for i, item in enumerate(nums):
            if one:
                if item <= one[1]:
                    one = (i, item)
                    continue

                if two :
                    if item <= two[1]:
                        two = (i, item)
                    else:
                        return True
                else:
                    two = (i, item)

            else:
                one = (i, item)

        return False
