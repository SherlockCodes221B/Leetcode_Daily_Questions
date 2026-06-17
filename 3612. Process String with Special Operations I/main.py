'''
Input: s = "a#b%*"

Output: "ba"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
Thus, the final result is "ba".

Constraints:

1 <= s.length <= 20
s consists of only lowercase English letters and special characters *, #, and %.
'''



class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for x in s:
            if x == "#":
                result  = self.duplicates(result)
            elif x == "%":
                result = self.reverse(result)
            elif x == "*":
                result = self.remove(result)
            else:
                result += x
        return result

    def remove(self, res):
        res = res[:-1]
        return res
    
    def duplicates(self, res):
        res = res + res
        return res


    def reverse(self, res):
        res = res[::-1]
        return res
