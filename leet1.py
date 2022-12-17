# 1422. Maximum Score After Splitting a String
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
# Example
# Input: s = "011101"
# Output: 5
# Explanation:
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5
# left = "01" and right = "1101", score = 1 + 3 = 4
# left = "011" and right = "101", score = 1 + 2 = 3
# left = "0111" and right = "01", score = 1 + 1 = 2
# left = "01110" and right = "1", score = 2 + 1 = 3

# my solution -69ms
class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            ll = left.count('0')
            rl = right.count('1')
            if ll + rl > max:
                max = ll + rl
        return max

# best solution -25ms
class Solution:
    def maxScore(self, s: str) -> int:
        size = len(s)
        zeros, ones = [0] * size, [0] * size
        if s[0] == '0':
            zeros[0] = 1
        if s[size - 1] == '1':
            ones[size - 1] = 1
        for i in range(1, size):
            ones[size - 1 - i] = ones[size - i]
            zeros[i] = zeros[i - 1]
            if s[size - 1 - i] == '1':
                ones[size - 1 - i] += 1
            if s[i] == '0':
                zeros[i] += 1
        max_score = 0
        for i in range(size - 1):
            score = ones[i + 1] + zeros[i]
            if score > max_score:
                max_score = score
        return max_score

    # personal fav
    class Solution:
        def maxScore(self, s: str) -> int:
            x = int(s[0] == '0') + s[1:].count('1')
            res = [x] + [(x := x + 1) if c == '0' else (x := x - 1) for c in s[1:-1]]
            return max(res)