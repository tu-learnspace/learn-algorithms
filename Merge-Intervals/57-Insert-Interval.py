"""
https://leetcode.com/problems/insert-interval
Đề ======
Intervals đã được sort. Insert newInterval vào intervals.

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Idea ======
Intervals đã được sort:
- Tìm chỗ start nào chen vô được
-> Add những chỗ có curr.end < new_interval.start và curr.start > new_interval.end:
___________           ________________________
[0,1] [2,3]   [5,7]   [9,12] [13, 14] [15, 16]
               [6,8]
- Chỗ cần merge thì có các TH: cứ adjust a và b là thấy được điều kiện thỏa.
a:    _____
b:      ___
Note rằng, merge xong còn có thể merge tiếp. Vd:
   [5,7] [8,10]
[4, 12]

Phải thỏa luôn TH chèn vô mà ko merge:
[1,3]        [6,7] [8,12]
       [4,5]
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged_intervals = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1

        # Merge all intervals that are qualified to merge.
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged_intervals.append(newInterval)

        # ko cần `and newInterval[1] < intervals[i][0]`
        while i < len(intervals):
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals

if __name__ == '__main__':
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    intervals = [[0,1], [2,3], [5,7], [8,12], [13,14], [15,16]]
    newInterval = [4,6]
    res = Solution().insert(intervals, newInterval)
    print(res)
