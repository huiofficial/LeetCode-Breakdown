class Solution:
    def convert(self, char):
        if char == "I": return 1
        elif char == "V": return 5
        elif char == "X": return 10
        elif char == "L": return 50
        elif char == "C": return 100
        elif char == "D": return 500
        elif char == "M": return 1000
        else: print("wrong character: ", char, "!")

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i, char in enumerate(s):
            if char == "I" and i < len(s)-1:
                if s[i+1] == "V" or s[i+1] == "X":
                    res -= 1
                else: res += self.convert(char)
            elif char == "X" and i < len(s)-1:
                if s[i+1] == "L" or s[i+1] == "C":
                    res -= 10
                else: res += self.convert(char)
            elif char == "C" and i < len(s)-1:
                if s[i+1] == "D" or s[i+1] == "M":
                    res -= 100
                else: res += self.convert(char)
            else: res += self.convert(char)

        return res
