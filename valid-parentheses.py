class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i, item in enumerate(s):
            if item == "(" or item == "[" or item =="{":
                stack.append(item)
            else:
                if stack == []: return False
                elif item == ")" and stack.pop() != "(": return False
                elif item == "]" and stack.pop() != "[": return False
                elif item == "}" and stack.pop() != "{": return False
                else: pass

        if stack != []: return False
        else: return True
