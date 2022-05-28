'''
273. Integer to English Words - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Hard
Submission: 28 ms; 14.3 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

def helper_function(num: int):
    # returns the english version of 1-3 numbers
    # if num == 0, returns empty string
    
    sub_twenty = {
        1: "One ",
        2: "Two ",
        3: "Three ",
        4: "Four ",
        5: "Five ",
        6: "Six ",
        7: "Seven ",
        8: "Eight ",
        9: "Nine ",
        10: "Ten ",
        11: "Eleven ",
        12: "Twelve ",
        13: "Thirteen ",
        14: "Fourteen ",
        15: "Fifteen ",
        16: "Sixteen ",
        17: "Seventeen ",
        18: "Eighteen ",
        19: "Nineteen ",
    }
    
    # TODO: could merge gte_twenty with sub_twenty with each 
    # key in gte_twenty multiplied by ten and each key in 
    # calls to gte_twenty multiplied by ten
    gte_twenty = {
        2: "Twenty ",
        3: "Thirty ",
        4: "Forty ",
        5: "Fifty ",
        6: "Sixty ",
        7: "Seventy ",
        8: "Eighty ",
        9: "Ninety "
    }
    
    string = ''

    if num:

        # hundreds place if nonzero
        if len(str(num)) == 3 and int(num/100):
            string += sub_twenty[int(num/100)] + "Hundred "

        # tens place if 2 or greater
        if len(str(num)) >= 2 and int(num/10)%10 > 1:
            string += gte_twenty[int(num/10)%10]

        # tens place if 1 (the teens)
        if int(num/10)%10 == 1:
            string += sub_twenty[num%100]

        # ones place if nonzero and non-"teen"
        if num % 10 and int(num/10)%10 != 1:
            string += sub_twenty[num%10]

    return string
        
class Solution:
    def numberToWords(self, num: int) -> str:
        
        hashmap = {
            1: '',
            2: '',
            3: '',
            4: "Thousand ",
            5: "Thousand ",
            6: "Thousand ",
            7: "Million ",
            8: "Million ",
            9: "Million ",
            10: "Billion ",
            11: "Billion ",
            12: "Billion "
        }

        if not num:
            return "Zero"

        final_string = ''

        # loop through number length
        while num:

            # separate number into triplets, starting with greatest value to least value in the number
            # note: largest magnitude triplet may have less than 3 numbers in it
            triplet = num
            if len(str(num)) > 3:
                triplet = int(num / 10 ** ( len(str(num)) - 3 )) if len(str(num)) % 3 == 0 else int(num / 10 ** ( len(str(num)) - len(str(num)) % 3 ))

            # we then pass the triplet through an external function that generates a string based on the triplet; add it to string
            final_string += helper_function(triplet)

            # based on value magnitude of triplet, decide what to add after it (i.e., billion, million, thousand, '')
            final_string += hashmap[len(str(num))]

            # get rid of first "triplet" and return to loop condition. If this is the last triplet, set num equal to 0 to cause loop termination
            if len(str(num)) > 3:
                num = int(num % 10 ** ( len(str(num)) - 3)) if len(str(num)) % 3 == 0 else int(num % 10 ** ( len(str(num)) - len(str(num)) % 3 ))
            else:
                num = 0

        return final_string[:-1]
        