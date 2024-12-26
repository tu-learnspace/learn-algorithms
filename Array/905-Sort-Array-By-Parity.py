"""
https://leetcode.com/problems/sort-array-by-parity/

"""


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        next_odd, next_even = 0, len(nums) - 1

        while next_odd < next_even:
            if nums[next_odd] % 2 == 0:
                next_odd += 1
            else:
                nums[next_odd], nums[next_even] = nums[next_even], nums[next_odd]
                next_even -= 1


if __name__ == '__main__':
    arr1 = [3, 1, 2, 4]
    arr2 = [0]
    Solution().sortArrayByParity(arr1)
    Solution().sortArrayByParity(arr2)
    print(arr1) # [2, 4, 3, 1]
    print(arr2) # [0]