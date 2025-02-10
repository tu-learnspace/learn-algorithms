"""
https://leetcode.com/problems/merge-intervals/
Đề =========
Merge các overlapping interval.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Idea ==========
Sort các interval theo start.
Với a.start <= b.start thì có các TH sau khi merge (nếu overlap, ko thì thôi):

a: --
b:     ---
-> ko merge

a:	__
b: 	____
a:	__
b: 	  ____
-> [a.start, b.end]

a: 	_______
b:    ___
a: 	______
b:  ___
-> [a.start, a.end]

Start luôn a.start, end thì depend b.end hay a.end hơn

[1, 3], [2, 6], [5, 10], [15, 18]
  a        b                       # init
[1, 6] <- a        b               # update a.end
[1, 10] <- a                b      # update a.end
[1, 10], [15, 18]                  # add a to result
  a          b
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x[0])
        merged_intervals = []

        a_start = intervals[0][0]
        a_end = intervals[0][1]

        for i in range(1, len(intervals)):
            b_start = intervals[i][0]
            b_end = intervals[i][1]

            if b_start <= a_end: # overlap -> merge
                a_end = max(a_end, b_end)
            else: # ko overlap -> ko merge
                merged_intervals.append([a_start, a_end])
                a_start = b_start
                a_end = b_end

        merged_intervals.append([a_start, a_end])

        return merged_intervals

if __name__ == '__main__':
    #intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1,4],[5,6],[8,15],[10,18]]
    res = Solution().merge(intervals)
    print(res)
