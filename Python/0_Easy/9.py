'''
9. Palindrome Number - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Easy
Submission: 48 ms; 14.1 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]