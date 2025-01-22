"""
https://leetcode.com/problems/maximum-average-subarray-i
Đề ========
Cho array of nums. Tìm k-size sub array có max average.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Idea ========
Sliding window. Max average = max sum / len -> chỉ cần tính max sum là được vì len ko đổi.
Note: In Python 2: 5 / 2 gives 2 (integer result). In Python 3: 5 / 2 gives 2.5 (float result).
-> Use float(k) instead of k.
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        start = 0
        max_sum = float('-inf')
        curr_sum = 0
        for end in range(len(nums)):
            print('start ', start, ' end ', end, 'curr_sum ', curr_sum, ' nums[end] ', nums[end])
            curr_sum += nums[end]

            if end - start > k - 1:
                curr_sum -= nums[start]
                start += 1
                print('update start ', start, ' end ', end)

            max_sum = max(max_sum, curr_sum)
            print('start ', start, ' end ', end, ' max_sum: ', max_sum)

        return max_sum / float(k)

        # n=len(nums)
        #
        # window_sum = max_sum = sum(nums[:k])
        # print('window', window_sum)
        #
        # for i in range(n-k):
        #     window_sum = window_sum - nums[i] + nums[i+k]
        #
        #     if window_sum > max_sum:
        #         max_sum = window_sum
        #
        # print('max sum', max_sum)
        # return max_sum/float(k)

        # max_avg = sum(nums[:k])
        # for i in range(len(nums) - k + 1):
        #     max_avg = max(max_avg, sum(nums[i:i + k]) / k)
        #
        # return max_avg


if __name__ == '__main__':
    # nums = [1, 12, -5, -6, 50, 3]
    # k = 4
    # # nums = [4, 0, 4, 3, 3]
    # # k = 5
    # res = Solution().findMaxAverage(nums, k)
    # print(res)
    num2 = [-6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284, -3024, 1714, -2825, -2374, -2750, -959, 6516,
     9356, 8040, -2169, -9490, -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337, -9158, -4183,
     6240, -2846, -2588, -5458, -9576, -1501, -908, -5477, 7596, -8863, -4088, 7922, 8231, -4928, 7636, -3994, -243,
     -1327, 8425, -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831, 2854, -4498, -6983, -677, 2216,
     -1938, 3348, 4099, 3591, 9076, 942, 4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296, -3280,
     8909, -8352, -9413, 3513, 1352, -8825] #93
    k2 = 90
    res2 = Solution().findMaxAverage(num2, k2)
    print(res2)
