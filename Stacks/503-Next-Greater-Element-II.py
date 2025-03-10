"""
https://leetcode.com/problems/next-greater-element-ii
Đề =========
Tìm next greater element của mọi phần tử mảng.
Next greater element là element tiếp theo lớn hơn trong mảng.

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
Bắt đàu từ cuối vì phần tử cuối k có next greater nên cuối cùng luôn là -1.

[13, 14, 7, 6, 12]

"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        res = [-1] * len(nums)

        for i in range(len(nums) - 1, -1 , -1):
            while s and s[-1] <= nums[i]:
                s.pop()

            if s:
                res[i] = s[-1]
            s.append(nums[i])

        return res

if __name__ == '__main__':
    nums = [4, 5, 2, 25]
    res = Solution().nextGreaterElements(nums)
    print(res)
