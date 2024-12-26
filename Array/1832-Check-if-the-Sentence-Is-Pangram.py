"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

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
        #
        # for i in range(len(sentence)):
        #     currChar = sentence[i].lower()
        #
        #     if currChar.isalpha():
        #         seen.add(currChar)
        #
        # return len(seen) == 26


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    res = Solution().checkIfPangram(sentence)
    print(res)