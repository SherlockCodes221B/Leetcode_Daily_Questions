'''
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:

Input: s = "1"
Output: 0
 
'''

class Solution:
    def numSteps(self, s: str) -> int:
        i = 0
        number = int(s,2)
        count = 0
        if s == "1":
            return 0
        while number != 1:
            if number % 2 != 0:
                number = number + 1
                count = count + 1
            else:
                number = number // 2
                count = count + 1
        return count
'''

This is with Bruite force, there is a way to complicate this things suing stacks but no point. because brute and the stack approach gives the same time complexity. but differ in space complexity making brute force easier in this case
'''
