"""
https://leetcode.com/problems/subarray-product-less-than-k
Đề ======
Đếm số subarray mà tích các phần tử của nó bé hơn target. 1 <= nums[i] <= 1000
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Idea ======
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: # làm sao mà có 2 số nguyên cộng lại = 1 được
            return 0

        left = 0
        curr_product = 1
        count = 0

        for right in range(len(nums)):
            curr_product *= nums[right]

            while curr_product >= k and left <= right:
                curr_product /= nums[left]
                left += 1

            count += right - left + 1

        return count


if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    res = Solution().numSubarrayProductLessThanK(nums, k)
    print(res)
