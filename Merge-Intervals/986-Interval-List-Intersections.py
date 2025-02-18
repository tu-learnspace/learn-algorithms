"""
https://leetcode.com/problems/interval-list-intersections
Đề ======
Merge 2 list interval lại. Mỗi list disjoint và được sorted theo start.

Idea =====
Dùng 2 pointers để duyệt 2 danh sách. Dùng rule: 2 intervals intersect khi start của 1 cái lies trong cái còn lại.
"""
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        merged_intervals = []

        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            # 1st list overlap 2nd list or vice versa
            if (secondList[j][0] <= firstList[i][0] <= secondList[j][1] or
                    firstList[i][0] <=  secondList[j][0] <= firstList[i][1]):
                merged_intervals.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

            # a:  --    ---
            # b: -----
            # Cái end trc (bị merge rồi) thì đc move next
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return merged_intervals

if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = Solution().intervalIntersection(firstList, secondList)
    print(res) # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]