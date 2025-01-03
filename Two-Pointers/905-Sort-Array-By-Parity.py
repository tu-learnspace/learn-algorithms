"""
https://leetcode.com/problems/sort-array-by-parity/
Đề ======
Cho array, move all số chẵn ra đầu mảng trước rồi tới số lẻ theo sau
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Idea ======
1 con trỏ duyệt và 1 con trỏ giữ chỗ. Khi con trỏ duyệt tới chẵn thì swap với con trỏ giữ chỗ (chắc chắn là lẻ).
Cứ thế khi duyệt hết mảng sẽ make sure swap hết chẵn lên đầu.
"""
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = 0 # pointer giữ chỗ next-even element
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

        """
        C2: cũng là 2 con trỏ nhưng mà ở 2 đầu.
        """
        # next_even, next_odd = 0, len(nums) - 1
        # while next_even < next_odd:
        #     if nums[next_even] % 2 == 0:
        #         next_even += 1
        #     else:
        #         nums[next_even], nums[next_odd] = nums[next_odd], nums[next_even]
        #         next_odd -= 1
        # return nums

if __name__ == '__main__':
    arr1 = [3, 1, 2, 4]
    arr2 = [0]
    res1 = Solution().sortArrayByParity(arr1)
    res2 = Solution().sortArrayByParity(arr2)
    print(res1) # [2, 4, 3, 1]
    print(res2) # [0]