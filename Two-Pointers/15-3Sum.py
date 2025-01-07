"""
https://leetcode.com/problems/3sum
Đề =====
Tìm 3 số trong arr cộng lại = 0. Trả ra unique triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Idea =======
Sort array
Duyệt i toàn mảng, với mỗi i dùng method 2 pointers l & r để tìm sum = -i (để + lại = 0).
Vd: Với mỗi i ta có 2 sum l & r sao cho arr[l] + arr[r] = -arr[i]
 i   l        r
[-4,-1,-1,0,1,2]
     i  l     r
[-4,-1,-1,0,1,2]

Để loại bỏ triplets trùng: vì arr đã sort nên với mỗi bộ ba tìm được thì phần tử tiếp theo không giống phía trước thì sẽ không trùng
-> Với mỗi (i,l,r) đang xét, check phần tử hiện tại & phần tử trước nó không giống nhau mới làm.
"""
class Solution(object):
    def twoSum(self, arr, left, right, target, triplets):
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1
                # skip same element to avoid duplicate triplets
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        right = len(nums) - 1

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i + 1, right, -nums[i], triplets)

        return triplets


if __name__ == '__main__':
    numbers = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(numbers)
    print(res)