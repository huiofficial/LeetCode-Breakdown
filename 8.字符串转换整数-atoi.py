#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        sign = 1
        value = ""
        signFlag = 1
        for i in range(len(s)):
            if s[i] == " ": 
                if value=="":
                    continue
                else:
                    return 0
            elif s[i] == "-": 
                if signFlag:
                    sign = -1
                    signFlag = 0
                else:
                    return 0
            elif s[i] == "+": 
                if signFlag: 
                    sign = 1
                    signFlag = 0
                else:
                    return 0
            elif s[i] in digits:
                value += s[i]
            else:
                break
        print(value)
        if value == "": return 0
        ans = sign*(int(value))
        if ans < -2**31:
            return -2**31
        elif ans > 2**31:
            return 2**31-1
        else:
            return ans

# @lc code=end

