"""
https://leetcode.com/problems/interval-list-intersections
Đề ======
Merge 2 list interval lại. Mỗi list disjoint và được sorted theo start.

Idea =====

"""
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """


if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(firstList, secondList)
    print(res)