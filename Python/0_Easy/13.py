'''
13. Roman to Integer - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Easy
Submission: 44 ms; 14.3 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                sum += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                sum += values[s[i]]
                i += 1

        return sum