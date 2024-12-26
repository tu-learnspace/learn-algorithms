"""
https://leetcode.com/problems/reverse-bits/description/
Reverse bits of a given 32 bits unsigned integer.

"""


class Solution:
    def reverseBits(self, n):
        # 32 bits
        res = 0
        for i in range(32):
            res = res << 1
            res = res | (n & 1)
            n = n >> 1
        return res

    # def reverseBits2(self, n):
    #     MASK_SIZE = 16
    #     BIT_MASK = 0x7FFFF
    #     CACHE=[0] * (BIT_MASK + 1)
    #     return (
    #             CACHE[n & BIT_MASK] << (3 * MASK_SIZE) |
    #             CACHE[(n >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
    #             CACHE[(n >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
    #             CACHE[(n >> (3 * MASK_SIZE)) & BIT_MASK]
    #             )



if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits2(43261596))