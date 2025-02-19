"""
https://leetcode.com/problems/valid-parentheses
Đề ===========
Cho string gồm các loại brackets. Check nếu nó là valid parentheses (brackets có đóng mở)

Idea =============
Dùng stack đếm cặp:
- gặp open bracket thì push
- gặp close bracket thì pop

Nhờ check các TH đủ SL cặp đóng mở nhưng ko theo pair. Vd ({[}])
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0: # pop nhiều quá rồi nên còn gì đâu mà pop.
                    return False

                top = stack.pop()

                # TH là 1 cặp đóng mở nhưng ko cùng type. Vd ({[}]) -> đủ cặp đóng mở nhưng ko theo pair.
                if s[i] == ')'  and top != '(':
                    return False
                if s[i] == '}'  and top != '{':
                    return False
                if s[i] == ']'  and top != '[':
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    s = '({[]})'
    res = Solution().isValid(s)
    print(res)

    s = '({[}])'
    res = Solution().isValid(s)
    print(res)

    s2 = '(({)}]]}('
    res2 = Solution().isValid(s2)
    print(res2)

    s3 = '(]'
    res3 = Solution().isValid(s3)
    print(res3)