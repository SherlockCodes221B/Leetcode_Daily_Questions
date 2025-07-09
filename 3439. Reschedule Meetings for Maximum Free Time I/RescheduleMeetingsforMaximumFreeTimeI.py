'''
Very wierd solution I came across. I tried my code it doesn't work. Finally went to editor which made it more wierd
You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

The relative order of all the meetings should stay the same and they should remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.

 

Example 1:

Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

Output: 2

'''

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        res = 0
        total = [0]*(len(startTime)+1)
        for i in range(len(startTime)):
            total[i+1] = total[i] + endTime[i] - startTime[i]
        for i in range(k-1, len(startTime)):
            r = eventTime if i == len(startTime)-1 else startTime[i+1]
            l = 0 if i == k-1 else endTime[i-k]
            res = max( res, r-l-(total[i+1] - total[i-k+1]) )
        return res
