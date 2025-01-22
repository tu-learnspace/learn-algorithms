"""
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k
Đề ======
Cho array of nums. Tìm sub-array có size k mà sum element là lớn nhất.

Input: arr = [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Idea ======
Dùng sliding window. Vd:
2, 1, 5, 1, 3, 2
s     e
   s     e
-> Move window 3 này đi thì tận dụng đc 2 element ở giữa, chỉ cần trừ element rìa trái & cộng element rìa phải.
Dùng biến start, end để tạo window: start giữ nguyên, end duyệt trước.
"""
class Solution(object):
    def findMaxSumSubArray(self, k, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        max_sum = float('-inf')
        curr_sum = 0

        for end in range(len(nums)):
            curr_sum += nums[end]
            # Chỉ slide window khi vượt limit size k
            if end >= k - 1:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[start]
                start += 1

        return max_sum

if __name__ == '__main__':
    # nums = [2, 1, 5, 1, 3, 2]
    # k = 3
    nums = [1, 2, 3, 4, 5]
    k = 5
    res = Solution().findMaxSumSubArray(k, nums)
    print(res)