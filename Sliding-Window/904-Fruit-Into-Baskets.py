"""
https://leetcode.com/problems/fruit-into-baskets
Đề ======
Tính số quả nhiều nhất có thể thu hoạch. Input là array các tree. arr[i] là LOẠI quả tại cây thứ i.
Được cho 2 basket, mỗi basket chỉ đc 1 LOẠI quả, k giới hạn số trái.
Có thể bắt đầu từ bất kỳ cây nào. Tại mỗi cây chỉ đc pick 1 quả, move dần sang phải, không được skip cây.
Cứ pick tới khi nào ko thể tiếp tục.

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
Pick tới khi ko thể tiếp tục -> aka dừng khi pick loại quả thứ 3.
Dùng sliding window, tạo cửa sổ bằng cách expand bên phải, tới khi ko thỏa nữa thì shrink bên trái, cập nhật max, repeat.
"""
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruits_frequency = {}
        start = 0
        max_fruits = float('-inf')

        for end in range(len(fruits)):
            if fruits[end] not in fruits_frequency:
                fruits_frequency[fruits[end]] = 0

            fruits_frequency[fruits[end]] += 1

            while len(fruits_frequency) > 2:
                fruits_frequency[fruits[start]] -= 1
                if fruits_frequency[fruits[start]] == 0:
                    del fruits_frequency[fruits[start]]

                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits

if __name__ == '__main__':
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    res = Solution().totalFruit(fruits)
    print(res)