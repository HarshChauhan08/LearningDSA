# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

"""
Approach : hashmap (dictionary)

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i