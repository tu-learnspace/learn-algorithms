"""
https://leetcode.com/problems/valid-palindrome/

Note: dùng isalnum thay vì isalpha vì đề accept alphanumeric
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].lower().isalnum():
                i += 1
            while i < j and not s[j].lower().isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama!"
    s2 = "0P"
    res1 = Solution().isPalindrome(s1)
    res2 = Solution().isPalindrome(s2)
    print(res1, res2)