'''
680. Valid Palindrome II - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Easy
Submission: 192 ms; 14.6 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

import difflib

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        j = len(s) - 1
        
        for i in range(j):
            
            if s[i] != s[j]:
                
                i1 = i
                j1 = j - 1
                i2 = i + 1
                j2 = j
                
                while i1 < j1 and s[i1] == s[j1]:
                    i1 += 1
                    j1 -= 1
                
                if i1 >= j1:
                    return True
                
                while i2 < j2 and s[i2] == s[j2]:
                    i2 += 1
                    j2 -= 1
                    
                if i2 >= j2:
                    return True
                
                return False
            
            j -= 1
            
        return True