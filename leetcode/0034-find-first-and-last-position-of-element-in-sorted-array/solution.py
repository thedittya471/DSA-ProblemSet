# Runtime: 0 ms
# Memory: 13.2 MB

class Solution(object):
    def searchRange(self, nums, target):
        def find_bound(is_first):
            start, end = 0, len(nums) - 1
            bound = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        end = mid - 1
                    else:
                        start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]