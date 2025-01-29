"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
https://algo.monster/liteproblems/340
Đề =====
Cho chuỗi, tìm substring dài nhất có K kí tự

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Idea =====
Sliding window. Dùng counter để đếm.
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        a r a a c i
        """
        start, max_len, curr_len = 0, 0, 0
        hash_map = {}

        for end in range(len(s)):
            if s[end] not in hash_map:
                hash_map[s[end]] = 0
            hash_map[s[end]] += 1

            while len(hash_map) > k:
                hash_map[s[start]] -= 1
                if hash_map[s[start]] == 0:
                    del hash_map[s[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len

if __name__ == '__main__':
    str = 'araaci'
    k = 1
    res = Solution().lengthOfLongestSubstringKDistinct(str, k)
    print(res)
