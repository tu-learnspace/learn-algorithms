"""
https://leetcode.com/problems/valid-anagram/
# Đề ======
Cho 2 chuỗi, check xem phải là anagram không. Anagram là chữ xáo trộn vị trí thôi.
Input: s = "anagram", t = "nagaram"
Output: true

# Idea: =====
Dùng frequency map để check, tập dụng luôn 1 map đó. Nếu 2 thằng là anagram thì map phải bằng 0 hết.
-> 1 string mang đơn vị giá trị dương, string còn lại mang giá trị âm
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq = {}
        for i in range (len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            if t[i] in freq:
                freq[t[i]] -= 1
            else:
                freq[t[i]] = -1

        for char in freq:
            if freq[char] != 0:
                return False
        return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)