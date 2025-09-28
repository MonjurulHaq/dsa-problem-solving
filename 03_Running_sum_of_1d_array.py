# https://leetcode.com/problems/running-sum-of-1d-array/description/


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        arr = []
        for num in nums:
            s += num
            arr.append(s)
        return arr