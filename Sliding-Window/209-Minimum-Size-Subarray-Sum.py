"""
https://leetcode.com/problems/minimum-size-subarray-sum
Đề ==========
Cho array nums, tìm smallest subarray có sum >= target và trả ra length của nó. Nếu k có return 0

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Idea ==========
Dùng 2 con trỏ tạo sliding windows move dần, khi nào sum >= target thì update min. Do subarray là contiguous nên đảm bảo
được không miss element. ge
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start, curr_sum = 0, 0
        min_len = float('inf')
        for end in range(len(nums)):
            curr_sum += nums[end]

            if curr_sum >= target:
                curr_len = end - start + 1
                print('end ', end, '- start ', start, ' - len', curr_len)
                min_len = min(min_len, curr_len)
                curr_sum -= nums[start]
                start += 1

        return min_len

if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = Solution().minSubArrayLen(target, nums)
    print(res)