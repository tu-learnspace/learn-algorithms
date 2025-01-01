"""
https://leetcode.com/problems/two-sum/
# Đề: =========
Cho mảng, tìm tổng 2 phần tử = target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Idea: ==========
Dùng 2 pointers. Sort the input array
Lưu ý đề yêu cầu return index, not value -> save original index
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    """
    C1: 2 pointers
    """
    # Tạo indices từ 0 -> len - 1 rồi sort theo value trong nums
    # vd nums: [3, 2, 4] -> tạo [0, 1, 2] ứng với index của [3, 2, 4] -> sort [1, 0, 2]
    # vì khi khúc dưới sort nums lại sẽ thành [2, 3, 4] thì [1, 0, 2] tương ứng index cũ trước khi sort
    # -> trả về đc index cho đề bằng vị trí tương ứng
    indexes = sorted(range(len(nums)), key=lambda k: nums[k])
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [indexes[i], indexes[j]]

    return [-1, -1]
    """
    C2: Hash map
    Tìm X + Y = target. 
    Duyệt từng phần tử là X, nếu X + Y nào đó trong hash map thì có pair. 
    Aka nếu trong hash map có Y thỏa Y = target - X thì có pair (là Y và X hiện tại).
    -> Y chính là những cái X chưa thỏa lưu vào hash map <Y, Y's index>
    """
    # hash_map = {}
    # for i in range(len(nums)):
    #     if target - nums[i] in hash_map:
    #         return [hash_map[target - nums[i]], i]
    #     else: # lưu vào hash map index phần tử hiện tại (which chưa tìm được cặp)
    #         hash_map[nums[i]] = i
    # return [-1, -1]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3, 2, 4]
    # target = 6
    res = twoSum(nums, target)
    print(res)
