"""
https://leetcode.com/problems/power-of-two/

Constraints:
-2^31 <= n <= 2^31 - 1


Số 2^x có bit đầu tiên là 1, các bit còn lại là 0
2 = 2^1 = 1
4 = 2^2 = 10
8 = 2^3 = 100
16 =2^4 = 1000

C1: số 2^x AND với số trước nó sẽ ra 0.
Vì bản chất là do số phía trước đạt max là các số 1 rồi (01…1),
nên khi qua giá trị tiếp theo, nó sẽ là bội mới của 2 (10…0). Khi AND với nhau ra 0 hết.

C2: biết constraints độ dài bit thì dùng số lớn nhất (toàn là 11..1) module ra 0 thì là 2^x.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n & (n - 1) == 0:
            return True
        return False

    def isPowerOfTwo_2(self, n):
        if n <= 0:
            return False
        if (1 << 30) % n == 0: # max la 2^31
            return True
        return False


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(8))
    print(Solution().isPowerOfTwo(6))
    print(Solution().isPowerOfTwo_2(8))
    print(Solution().isPowerOfTwo_2(6))