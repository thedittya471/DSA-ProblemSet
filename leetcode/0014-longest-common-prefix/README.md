# 14. Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Trie-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2 ms |
| Memory | 12.2 MB |
| Submission Date | 2026-10-19T04:23:00.970Z |
| Platform | leetcode |

## Problem Statement

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= strs.length &lt;= 200</code>
- <code>0 &lt;= strs[i].length &lt;= 200</code>
- <code>strs[i]</code> consists of only lowercase English letters if it is non-empty.

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
