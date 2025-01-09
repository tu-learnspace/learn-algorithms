"""
https://leetcode.com/problems/subarray-product-less-than-k
Đề ======
Đếm số subarray mà tích các phần tử của nó bé hơn target.
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Idea ======
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
-> Nếu 5 * 2 * 6 thỏa < target thì các tập con của nó cũng thỏa.
[10, 5]: [10], [5] -> 2 cách = 2
[5, 2, 6]: [5, 2], [2, 6], [5], [2], [6] -> 5 cách = 3 + 2

[1,2,3,4] -> 1,2,3,4 / 1,2, 2,3, 3,4 / 1,2,3, 2,3,4 -> 9 cách = 4 + 3 + 2
[1,2,3,4,5] -> 1,2,3,4,5 / 1,2,3,4,  2,3,4,5, / 1,2,3,  2,3,4, 3,4,5 / 1,2 2,3 3,4, 4,5 -> 5 + 4 + 3 + 2 = 14 cách

 i    j
[10,5,2,6]
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    res = Solution().numSubarrayProductLessThanK(nums, k)
    print(res)
