"""
https://leetcode.com/problems/3sum-closest
Đề ======
Cho arr of nums & target, tìm bộ 3 số mà sum gần với target nhất. Assume mỗi input chỉ có 1 solution
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Idea ======
Giống 3sum: với 2 i ta dùng 2 pointer left right tiến dần về nhau.
  i  l    r
[2, 5, 6, 7] target = 16 (2+6+7=15)

"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_gap = float('inf') # min_gap cần min(target - curr_sum) min nhất có thể
        result = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_gap = abs(target - curr_sum)

                if curr_gap <= min_gap:
                    min_gap = curr_gap
                    result = curr_sum

                if curr_sum > target:
                    right -= 1
                else:
                    left += 1

        return result

if __name__ == '__main__':
    # nums = [-1, 2, 1, -4]
    # target = 1
    # nums = [1, 1, 1, 0]
    # target = -100
    nums = [2, 5, 6, 7]
    target = 16
    res = Solution().threeSumClosest(nums, target)
    print(res)