"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Đề ====
Cho mảng đã sort tăng dần, return mảng bình phương của mỗi phần tử in sort tăng dần
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

# Idea ====
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        C1: sort array. O(NlogN)
        """
        # return sorted([num*num for num in nums])

        """
        C2: Không dùng sort, dùng 2 pointers. O(N)
        Vd  [-4,-1,0,3,10] -> 2 phần tử ở rìa (xét chiều tiến dần về 0) chắc chắn khi ^2 lên là lớn nhất
        -> dùng 2 con trỏ ở 2 đầu để so sánh ai lớn hơn rồi push về cuối mảng mới
        """
        i, j = 0, len(nums) - 1
        curr_position = j # start at the end (max)
        res = [0 for _ in range(len(nums))]

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[curr_position] = nums[i]*nums[i]
                i += 1
            else:
                res[curr_position] = nums[j]*nums[j]
                j -= 1

            curr_position -= 1

        return res

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    result = Solution().sortedSquares(nums)
    print(result)
