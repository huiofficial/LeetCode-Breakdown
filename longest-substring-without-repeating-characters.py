class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        i = count = max_count = 0
        while i < len(s):
            if s[i] not in dict:
                dict[s[i]] = i
                count += 1
            else:
                i = dict[s[i]] + 1
                del(dict)
                dict = {}
                dict[s[i]] = i
                max_count = max(count, max_count)
                count = 1
            i += 1

        max_count = max(count, max_count)
        return max_count
