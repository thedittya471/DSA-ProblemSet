# Runtime: 16 ms
# Memory: 13.2 MB

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        d = {}
        for ch in s:
            if ch in d: d[ch] += 1
            else: d[ch] = 1

        arr = []
        for ch, f in d.items():
            arr.append([f, ch])
        arr.sort(reverse = True)
        print(arr)
        final = []
        for f, ch in arr:
            final.append(ch*f)
        print(final)
        return "".join(final)        