# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                c += 1
        return c