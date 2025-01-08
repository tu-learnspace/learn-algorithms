"""
https://leetcode.com/problems/3sum-smaller
Đề =======
Cho arr of numbers (chưa sort). Count all triplets (i,j,k) cộng lại bé hơn target
Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Idea ========
Giống 3Sum.
  i  l     r
[-1, 0, 2, 3] -> nếu -1,0,3 đã thỏa thì -1,0,2 chắc chắn thỏa (vì 2 < 3)

Điểm đặc biệt của bài này như case dưới này (mới vô đã thỏa): vì mảng đã được sort tăng dần
-> nếu khoảng [i..j] đã thỏa thì phần tử x ở giữa i, j cũng thỏa luôn (chắc chắn sẽ nhỏ hơn vì x < j nên sum sẽ bé hơn)
-> thay vì count += 1, ta dùng count += j - i
"""
class Solution:
    def searchTriplets(self, arr, target):
        if len(arr) < 3:
          return 0

        count = 0
        arr.sort()
        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                if curr_sum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

if __name__ == '__main__':
    nums = [-1, 0, 2, 3]
    target = 3
    res = Solution().searchTriplets(nums, target)
    print(res)