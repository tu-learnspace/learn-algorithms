"""
https://leetcode.com/problems/remove-element/
# Đề ======
Remove phần tử khỏi mảng in-place. Các phần tử còn lại dồn lên đầu array, thứ tự không quan trọng.
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

# Idea =====
Ý tưởng giống LC-26: ngoài con trỏ duyệt, xài 1 con trỏ để giữ vị trí cho next-non-deleted.
Note that đề không quan tâm của các element còn lại, vì cách trên sẽ không loại bỏ hoàn toàn các phần tử cuối = val,
nhưng nó sẽ chắc chắn TẤT CẢ các phần tử đầu khác val.

Vd: val=2, i để duyệt, j để giữ vị trí
 ij
[0,1,2,2,3,0,4,2] - assign
   ij
[0,1,2,2,3,0,4,2] - assign
     ij
[0,1,2,2,3,0,4,2] - ko assign nữa
     j   i
[0,1,2,2,3,0,4,2] - assign
     j   i
[0,1,3,2,3,0,4,2]
       j   i
[0,1,3,2,3,0,4,2]
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        next_non_removed = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[next_non_removed] = nums[i]
                next_non_removed += 1
        return next_non_removed

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    res = Solution().removeElement(nums, val)
    print(nums)


