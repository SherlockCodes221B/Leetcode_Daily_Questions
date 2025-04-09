'''
You are given an integer array nums and an integer k.
An integer h is called valid if all values in the array that are strictly greater than h are identical.
For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.
You are allowed to perform the following operation on nums:
Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

Example 1:
Input: nums = [5,2,5,4,5], k = 2
Output: 2
Explanation:
The operations can be performed in order using valid integers 4 and then 2.
better question : 

You're given an array nums and a target number k.
In one operation, you can:
  Pick a number h, such that all numbers greater than h are the same
  Then change those greater numbers to h
Your goal is to make all numbers in the array equal to k using as few operations as possible.
Return the minimum number of operations needed, or -1 if it's not possible.
For Test Case 1:
nums = [5, 2, 5, 4, 5] and k = 2,
The elements > k are [4, 5], so in one operation we can convert all 5s to 4.
Note → We cannot pick 2 directly, because all numbers > h must be the same value, and the unique elements greater than 2 → [4, 5] — are different.

'''

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_Set = list(set(nums))
        c = 0
        for x in nums_Set:
            if x < k:   
                return -1
            elif x > k:
                c = c + 1
        return c
