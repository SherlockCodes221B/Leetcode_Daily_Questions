"""
Input: s = "a#b%*", k = 1

Output: "a"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
The final result is "ba". The character at index k = 1 is 'a'.

Example 2:

Input: s = "cd%#*#", k = 3

Output: "d"

Explanation:

i	s[i]	Operation	Current result
0	'c'	Append 'c'	"c"
1	'd'	Append 'd'	"cd"
2	'%'	Reverse result	"dc"
3	'#'	Duplicate result	"dcdc"
4	'*'	Remove the last character	"dcd"
5	'#'	Duplicate result	"dcddcd"
The final result is "dcddcd". The character at index k = 3 is 'd'.

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters and special characters '*', '#', and '%'.
0 <= k <= 1015
The length of result after processing s will not exceed 1015.
"""




class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        ln = 0

        for c in s:
            if c == '*':
                ln = max(ln - 1, 0)
            elif c == '#':
                ln *= 2
            elif c != '%':
                ln += 1

        if k >= ln:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '*':
                ln += 1
            elif c == '#':
                if k >= ln // 2:
                    k -= ln // 2
                ln //= 2
            elif c == '%':
                k = ln - 1 - k
            else:
                if ln == k + 1:
                    return c
                ln -= 1