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
Ta cứ trữ list các phần tử là candidate cho NGE vào stack, tới khi nào gặp 1 phần tử nào có thể lớn hơn cả candidate thì
cứ pop dần candidate ra.

[13,14,5,7,6,12]
[-1,-1,-1,-1,-1]         {12]

12 lớn hơn 6 nên đưa 12 vô res. Sau đó push 6 vô để check sau (biết đâu 6 là NGE của ai đó)
[13,14,5,  7, 6, 12]
[-1,-1,-1,-1,12, -1]   {6, 12]

7 lớn hơn 6 nên phải pop những phần tử bé hơn 7 ra, cho vào res (which is 12), sau đó đưa 7 vào
[13,14,5, 7, 6, 12]
[-1,-1,-1,12,12,-1]   {7, 12]

5 ko bé hơn 7 nên cho 7 vô res
[13,14,5, 7, 6, 12]
[-1,-1,7,12,12,-1]   {7, 12]

Tương tự, 14 lớn hơn nên cho pop ra hết, empty stack
[13,14,5, 7, 6, 12]
[-1,-1,7,12,12,-1]   {14]
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
    # nums = [4, 5, 2, 25]
    nums = [13,14,5,7,6,12]
    res = Solution().nextGreaterElements(nums)
    print(res)
