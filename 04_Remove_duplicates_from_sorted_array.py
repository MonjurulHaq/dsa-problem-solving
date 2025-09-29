# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j +=1
        return j