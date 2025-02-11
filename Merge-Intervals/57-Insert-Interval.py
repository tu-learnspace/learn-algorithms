"""
https://leetcode.com/problems/insert-interval
Đề ======

Intervals đã được sort

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Idea ======
Intervals đã được sort:
- Tìm chỗ start nào chen vô được -> bỏ qua những chỗ có end < new_interval.start
[0,1] [2,3]   [5,7] [8,12]
            [4,6]

- Bài toán quay vô các TH:
  [5,7]
[4,6]

 [5,7]
  [6,8]

 [4,   8]   [7, 10]
  [5,6]
 [4, 8] [7, 10]


TH chèn vô mà ko merge:
[1,3]       [6,7] [8,12]
      [4,5]
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                continue

            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])

            intervals[i][0] = start
            intervals[i][1] = end

        return intervals


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    res = Solution().insert(intervals, newInterval)
    print(res)
