"""
https://leetcode.com/problems/max-consecutive-ones-iii
Đề ====
Cho array of bit

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Idea =====

"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """ 
          .       .
        1,1,1,0,0,0,1,1,1,1,0
        """
        start, max_len, max_repeated_one = 0, 0, 0

        for end in range(len(nums)):
            if nums[end] == 1:
                max_repeated_one += 1

            while end - start + 1 > k + max_repeated_one:
                start += 1
                if nums[start] == 1:
                    max_repeated_one -= 1



            max_len = max(max_len, end - start + 1)
        return max_len

if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    res = Solution().longestOnes(nums, k)
    print(res)