# Runtime: 137 ms
# Memory: 20.8 MB

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count=0
        for val in costs:
            if val<=coins:
                count+=1
                coins -= val
        return count