"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

Idea: 3 cách
C1 BF: với mỗi phần tử, so sánh nó với tất cả các phần từ còn lại phía sau -> O(N^2)
C2: Dùng set() -> O(N)
C3: Dùng sort arr rồi ss 2 phần tử liền kề
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}

        for a in s:
            hash_map[a] = hash_map.get(a, 0) + 1

        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = "leetcode"
    res = Solution().firstUniqChar(s)
    print(res)