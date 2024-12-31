"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            curr_sum = numbers[i] + numbers[j]

            if curr_sum == target:
                return [i + 1, j + 1]

            if curr_sum > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3, 2, 4]
    # target = 6
    res = Solution().twoSum(nums, target)
    print(res)