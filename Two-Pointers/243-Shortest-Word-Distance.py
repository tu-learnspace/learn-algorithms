"""
https://leetcode.com/problems/shortest-word-distance
# Đề =========
Given an array of strings words and two different strings that already exist in the array word1 and word2, return the
shortest distance between these two words in the list.

Example 1:
Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
Output: 5
Explanation: The distance between "fox" and "dog" is 5 words.

Example 2:
Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
Output: 1
Explanation: The shortest distance between "a" and "b" is 1 word. Please note that "a" appeared twice.

Example 3:
Input: words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"
Output: 4
Explanation: The distance between "a" and "e" is 4 words.

Constraints:
2 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
word1 and word2 are in words.
word1 != word2

# Idea ======
Dùng 2 con trỏ để indicate vị trí của 2 từ. Khi nào con trỏ có vị trí thì tính độ dài để cuối cùng ra min.
Note: Ko lo nếu bị gặp lại string vì cứ duyệt từ i nhỏ tới lớn nên nếu tìm được thêm thì distance cũng sẽ càng min đi thôi.
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        distance = len(words)
        word1_idx = -1
        word2_idx = -1

        for i in range(len(words)):
            if words[i] == word1:
                word1_idx = i
            elif words[i] == word2:
                word2_idx = i

            if word1_idx != -1 and word2_idx != -1:
                distance = min(distance, abs(word1_idx - word2_idx))

        return distance


if __name__ == '__main__':
    # words = ["a", "c", "d", "b", "a"]
    # words1 = "a"
    # words2 = "b"
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word1 = "fox"
    word2 = "dog"
    res = Solution().shortestDistance(words, word1, word2)
    print(res)