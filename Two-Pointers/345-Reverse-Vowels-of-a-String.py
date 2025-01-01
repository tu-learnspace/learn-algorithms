"""
https://leetcode.com/problems/reverse-vowels-of-a-string
# Đề =====
Cho string s, đảo ngược vị trí mọi nguyên âm của string đó.
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Idea ======
Đảo ngược cả arr bằng cách đảo dần từ 2 rìa.
['I', 'e', 'o', 'A'] -> ['A', 'e', 'o', 'I'] -> -> ['A', 'o', 'e', 'I']
-> Xài 2 con trỏ để duyệt 2 đầu, khi gặp phụ âm thì swap
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        arr = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            # tìm tới khi gặp đc vowel
            while i < j and vowels.find(arr[i]) == -1:
                i += 1
            # tương tự với pointer còn lại
            while i < j and vowels.find(s[j]) == -1:
                j -= 1

            # đã gặp được (nên mới thoát if)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return "".join(arr)

if __name__ == '__main__':
    s = "hello"
    res = Solution().reverseVowels(s)
    print(res)