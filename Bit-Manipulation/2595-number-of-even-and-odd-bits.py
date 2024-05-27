"""
https://leetcode.com/problems/number-of-even-and-odd-bits/
tính số bit 1 ở vị trí chẵn & lẻ của số n

Dùng XOR 1 để liên tục switch giữa 1 & 0
"""


class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0, 0]
        i = 0

        while n:
            res[i] += n & 1
            n >>= 1
            i ^= 1

        return res


if __name__ == '__main__':
    print(Solution().evenOddBit(17))