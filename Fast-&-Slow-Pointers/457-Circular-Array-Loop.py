"""
https://leetcode.com/problems/circular-array-loop
Đề =====
Cho array, tại i thì arr[i] là số bước phải đi tiếp (dương tiến tới, âm lùi lại). Assume việc di chuyển là circular (tới cuối
thì vòng về đầu & ngc lại). Check xem array có cycle không:
- Cycle phải có ít nhất 1 element.
- Cycle chỉ được đi 1 hướng.
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0. Hướng đi chỉ có 1 hướng tiến tới.

Input: [2, 1, -1, -2]
Output: false
Explanation: Mặc dù có vẻ có cycle ở 1, 2 nhưng vì đi 2 hướng tới & lùi nên ko tính.

Input: nums = [1,-1,5,1,4]
Output: true
Explanation: có 3 cycle ở đây:
- cycle 0,1 thì bị 2 hướng
- cycle 2 thì chỉ có 1 element là nó (5 move 5 bước cũng ra 5)
- cycle 3 -> 4 -> 3: valid

Idea ======
Ở vd 3, cycle có thể ở bất cứ element nào -> phải duyệt all, mỗi element check for cycle.

1 2 -1 2 2
"""
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            fast, slow = i, i
            is_forward = nums[i] >= 0

            while True:
                slow = (slow + nums[slow]) // len(nums)
                fast = (fast + nums[fast]) // len(nums)


                fast = (fast + nums[fast]) // len(nums)




if __name__ == '__main__':
    # arr = [1, 2, -1, 2, 2]
    arr = [2, 1, -1, -2]
    res = Solution().circularArrayLoop(arr)
    print(res)