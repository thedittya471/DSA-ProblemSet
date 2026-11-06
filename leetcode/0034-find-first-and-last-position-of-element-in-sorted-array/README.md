# 34. Find First and Last Position of Element in Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 13.2 MB |
| Submission Date | 2026-11-06T20:09:05.752Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p>
```

**Example 3:**

```
</p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code>
- <code>nums</code> is a non-decreasing array.
- <code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
