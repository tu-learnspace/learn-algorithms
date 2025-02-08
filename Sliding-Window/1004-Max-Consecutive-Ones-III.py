"""
https://leetcode.com/problems/max-consecutive-ones-iii
Đề ====
Cho array of bit

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Idea =====
Sliding window y như longest repeating character replacement: maintain start vs end là window's boundaries. Expand window
bằng cách move end sang phải, khi nào vượt quá k thì shrink bên trái để có đk at most k -> đảm bảo keep track longest
subarray mà không cần check all possible subarray.
Tuy nhiên, đỡ hơn là chỉ có 0 vs 1 nên k cần hash map để store frequency.
"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, max_len, max_repeated_one = 0, 0, 0

        for end in range(len(nums)):
            if nums[end] == 1:
                max_repeated_one += 1

            while end - start + 1 > k + max_repeated_one:
                if nums[start] == 1:
                    max_repeated_one -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len

if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    res = Solution().longestOnes(nums, k)
    print(res)