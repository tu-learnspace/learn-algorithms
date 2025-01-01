"""
https://leetcode.com/problems/contains-duplicate
# Đề: =========
Check mảng có chứa phần tử lặp lại không

# Idea: ==========
- Dùng Set (hash map, là data structure k có duplicate element)
"""
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))
    """
    Đối với việc nums có thể quá lớn (thay vì tạo cả set ngay từ đầu hơi tốn) thì có thể consider duyệt
    từng element rồi check in hash.
    """
    # unique_set = set()
    # for x in nums:
    #     if x in unique_set:
    #         return True
    #     unique_set.add(x)  # Add the current element to the set
    # return False

if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = containsDuplicate(nums)
    print(res)
