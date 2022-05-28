'''
1. Two Sum - https://leetcode.com/problems/integer-to-english-words/
Difficulty: Easy
Submission: 56 ms; 15.4 MB

Made by Gian Zignago (https://leetcode.com/zignago/) on 10/31/2021
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):  # loops through indices in nums
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i