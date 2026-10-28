# 451. Sort Characters By Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Bucket_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 16 ms |
| Memory | 13.2 MB |
| Submission Date | 2026-10-28T09:40:34.085Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.</p>

<p>Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;tree&quot;
<strong>Output:</strong> &quot;eert&quot;
<strong>Explanation:</strong> &#39;e&#39; appears twice while &#39;r&#39; and &#39;t&#39; both appear once.
So &#39;e&#39; must appear before both &#39;r&#39; and &#39;t&#39;. Therefore &quot;eetr&quot; is also a valid answer.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;cccaaa&quot;
<strong>Output:</strong> &quot;aaaccc&quot;
<strong>Explanation:</strong> Both &#39;c&#39; and &#39;a&#39; appear three times, so both &quot;cccaaa&quot; and &quot;aaaccc&quot; are valid answers.
Note that &quot;cacaca&quot; is incorrect, as the same characters must be together.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;Aabb&quot;
<strong>Output:</strong> &quot;bbAa&quot;
<strong>Explanation:</strong> &quot;bbaA&quot; is also a valid answer, but &quot;Aabb&quot; is incorrect.
Note that &#39;A&#39; and &#39;a&#39; are treated as two different characters.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code>
- <code>s</code> consists of uppercase and lowercase English letters and digits.

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)
