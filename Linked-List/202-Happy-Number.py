"""
https://leetcode.com/problems/happy-number/

divmod là hàm trả về 2 giá trị: phần nguyên và phần dư
VD: divmod(10, 3) -> (3, 1) (10//3 = 3, 10%3 = 1)
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1




if __name__ == '__main__':
    print(Solution().isHappy(19))