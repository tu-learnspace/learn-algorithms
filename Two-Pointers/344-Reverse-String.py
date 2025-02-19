"""
https://leetcode.com/problems/reverse-string
Đề ========
Đảo ngược chuỗi in-place.

Idea ========
2 pointers or stack.
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # C1: 2 pointers
        i, j = 0, len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1

        # C2: push vô stack rồi pop ra. Nhưng cách này ko in-place edit string.
        # stack = list(s)
        # reversed_str = ''
        #
        # while stack:
        #     reversed_str += stack.pop()
        #
        # return reversed_str

if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)