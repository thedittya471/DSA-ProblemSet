# Runtime: 1181 ms
# Memory: 24.8 MB

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        max_sum = 0

        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])

        return max_sum
        