"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Đề: =========
Cho mảng đã sort tăng dần, loại bỏ các phần tử bị lặp in-place (edit array luôn).
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_] Những chỗ _ không quan tâm value.

# Idea: ==========
Duyệt mảng tuần tự nhưng dùng 2 con trỏ:
- 1 con để duyệt hết mảng
- con còn lại giữ chỗ next-non-dup mang ý nghĩa giữ chỗ phần tử tiếp theo ko dup, ta sẽ dùng con trỏ #1 để tìm nó.
Tìm được thì đưa giá trị #1 (current) vô #2 (slot giữ chỗ) rồi tăng #2 lên 1 (next slot).

Vd: i là con duyệt, j là next-non-dup để đánh dấu nên đứng yên đó thôi.
 i  j
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ij
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    j  i
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> arr[next-non-dup] != arr[i] -> vị trí có phẩn tử k dup nữa
    j  i
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4] -> copy
       ji
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4] -> tăng next-non-dup lên

tương tự:
       j        i
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]  -> arr[next-non-dup] =! arr[i]
       j        i
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4] -> copy
          j     i
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4] -> tăng next-non-dup lên

Vì mảng đã sort nên mình đảm bảo được không có vụ bị lặp lại sau khi assign (vì đã gặp phần tử khác rồi, aka phần
tử lớn hơn nó thì làm gì gặp lại nó nữa).
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next_non_dup = 1 # non-dup element tiếp theo chắc chắn là 1 (trừ cái đầu đi)
        for i in range(len(nums)):
            if nums[i] != nums[next_non_dup - 1]:
                nums[next_non_dup] = nums[i]
                next_non_dup += 1

        return next_non_dup

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = Solution().removeDuplicates(nums)
    print(res)
    print(nums)