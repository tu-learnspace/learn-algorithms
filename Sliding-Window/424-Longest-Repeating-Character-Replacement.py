"""
https://leetcode.com/problems/longest-repeating-character-replacement
Đề =========
Cho chuỗi s và int k. Có thể được replace tối đa k lần bất kỳ char nào của chuỗi s. Tìm length của same letter substring dài nhất.

Input: str="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: str="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

Idea =======
Dùng sliding windows.
Điều kiện để shrink: đếm max repeated char trong window đó. -> số còn lại là số char ta được replace đi.
số còn lại này ko được vượt quá k -> nếu vượt quá thì ta shrink lại.

k = 2
  .       .
a a b c c b b
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        max_repeated_char, max_len = 0, 0
        char_freq = {}

        for end in range(len(s)):
            if s[end] not in char_freq:
                char_freq[s[end]] = 0
            char_freq[s[end]] += 1

            max_repeated_char = max(max_repeated_char, char_freq[s[end]])

            while end - start + 1 > max_repeated_char + k:
                char_freq[s[start]] -= 1 # k cần del char_freq[s[start]] khi nó == 0 vì chỉ dùng nó để update max
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len

if __name__ == '__main__':
    str = "aabccbb"
    k = 2
    res = Solution().characterReplacement(str, k)
    print(res)