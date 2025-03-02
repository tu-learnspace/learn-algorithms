"""
https://leetcode.com/problems/next-greater-element-ii
Đề =========
Tìm next greater element của mọi phần tử mảng.
Next greater element là element tiếp theo lớn hơn trong mảng (theo thứ tự duyệt, có thể circular đc)

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Input: [4, 5, 2, 25]
Output: [5, 25, 25, -1]

Input: [13, 7, 6, 12]
Output: [-1, 12, 12, -1]

Idea ========
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        res = [-1] * len(nums)

        return res

if __name__ == '__main__':
    nums = [4, 5, 2, 25]
    res = Solution().nextGreaterElements(nums)
    print(res)
