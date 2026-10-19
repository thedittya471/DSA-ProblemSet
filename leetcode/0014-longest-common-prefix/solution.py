# Runtime: 2 ms
# Memory: 12.2 MB

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        res = ""
        for i in range(len(strs[0])):
            val = strs[0][i]
            is_true = True
            for j in range(len(strs) - 1):
                if i >= len(strs[j + 1]) or strs[j][i] != strs[j + 1][i]:
                    is_true = False
                    break

            if is_true:
                res += val
            else:
                break

        return res