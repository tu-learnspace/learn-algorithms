"""
https://leetcode.com/problems/fruit-into-baskets
Đề ======
Tính số quả nhiều nhất có thể thu hoạch. Input là array các tree. arr[i] là loại quả tại cây thứ i.
Được cho 2 basket, mỗi basket chỉ đc 1 loại quả, k giới hạn số trái.
Có thể bắt đầu từ bất kỳ cây nào. Tại mỗi cây chỉ đc pick 1 quả, move dần sang phải, không được skip cây.
Cứ pick tới khi nào ko thể tiếp tục aka pick loại quả thứ 3.

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2]. If we had started at the first tree, we would only pick from trees [0,1].

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2]. If we had started at the first tree, we would only pick from trees [1,2].

Idea =====
"""
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
if __name__ == '__main__':
