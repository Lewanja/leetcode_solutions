# """
# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#     Input: s = "()"
#     Output: true
#
# Example 2:
#     Input: s = "()[]{}"
#     Output: true
#
# Example 3:
#     Input: s = "(]"
#     Output: false
#
# Constraints:
#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.
# """

# Runtime 28 msBeats 85.68% Memory 14 MB
class Solution:
    def isValid(self, s: str) -> bool:
        open_symbols = ['(', '{', '[']
        stack=[]
        for char in s:
            if char in open_symbols:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char==")" and stack[-1]=="(":
                    stack.pop()
                elif char == "}" and stack[-1] =="{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        print(stack)
        return not stack

ans = Solution().isValid('(])')
print(ans)