# https://leetcode.com/problems/rotate-array

class Solution(object):
   def rotate(self, nums, k):
       k = k % len(nums)      
       r = len(nums) - k
       new = nums[0:r]
       nums[0:r] = []
       nums.extend(new)
       
# or
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]