"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# Đề =======
Check chuỗi là pangram không. Pangram là chuỗi mà mỗi chữ cái chỉ xuất hiện 1 lần.

# Idea ======
Dùng hash map
"""
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
        """
        Nếu không muốn add hết vào set
        """
        # seen = set()
        # for i in range(len(sentence)):
        #     curr_char = sentence[i].lower()
        #     if curr_char.isalpha():
        #         seen.add(curr_char)
        #
        # return len(seen) == 26

if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    res = Solution().checkIfPangram(sentence)
    print(res)