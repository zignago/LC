'''
12. Integer to Roman - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Medium
Submission: 36 ms; 14.2 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        
        pairs = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
            
        roman = ''
        
        for key, value in pairs.items():
            while num >= key:
                num -= key
                roman += value
                

        return roman