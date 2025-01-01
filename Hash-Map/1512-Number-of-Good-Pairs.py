"""
https://leetcode.com/problems/number-of-good-pairs
# Đề =======
Cặp (i, j) là good pair khi nums[i] == nums[j] với i < j
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Idea =========
C1: Duyệt 2 vòng lặp: với mỗi nums[i], ta xét mọi thằng còn lại
C2: Dùng hashmap.
"""
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # C1: O(N^2)
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count

        # C2: Hashmap: O(N)
        """
        [1, 1, 1, 1] -> 6 pairs
        Nhận xét: Khi lần lượt xét từng phần tử 1, mỗi phần tử đều có thể cặp mới each previous, không xét thằng đầu tiên.
        -> 
        - Bỏ 1 vô hash map để count frequency, 
        - Mỗi lần gặp lại 1 thằng thì + với count hiện tại (đại diện có bao nhiêu thằng previous) - 1 (ko xét 
        thằng đầu tiên init).
        """
        count = 0
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
            count += map[n] - 1
        return count

if __name__ == '__main__':
    #nums = [1, 2, 3, 1, 1, 3]
    nums = [1, 1, 1, 1]
    res = Solution().numIdenticalPairs(nums)
    print(res)