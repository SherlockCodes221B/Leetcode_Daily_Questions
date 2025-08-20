'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

'''

class Solution:
    def isValid(self, s: str) -> bool:
        dic = { "}":"{",
                ")":"(",
                "]":"["} 
        stack = []
        for x in s:
            if x in dic.values():
                stack.append(x)
            elif x in dic.keys():
                if not stack or dic[x] != stack.pop():
                    return False
        return not stack
