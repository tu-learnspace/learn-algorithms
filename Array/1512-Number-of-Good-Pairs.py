"""
https://leetcode.com/problems/number-of-good-pairs

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

        # C2: Hashmap -> O(N)
        """
        Dùng hash map để lưu. VD: [1, 1, 1, 1] -> 6 pairs
        Put 1 vô hash map.
        Lần lượt xét từng phần tử 1, mỗi phần tử đều có thể cặp mới each previous, không xét thằng đầu tiên.
        -> Bỏ 1 vô hash map, mỗi lần gặp 1 thằng thì + vô (đại diện bao nhiêu previous).
        
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