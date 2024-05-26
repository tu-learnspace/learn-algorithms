"""
https://leetcode.com/problems/reverse-integer
Đảo ngược số nguyên.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
2^31 - 1 = 2147483647

C1: convert number sang string rồi duyệt ngược
C2: dùng phép chia lấy dư

Note: Python 2.6 above xai 0x7 cho decimal number
So 0x7FFFFFFF will right, 0xFFFFFFF will failed
"""


class Solution(object):
    def reverse(self, x):
        res, x_remain = 0, abs(x)  # giữ lại x dể lát check số âm thì thêm - phía trc
        while x_remain:
            res = res * 10 + x_remain % 10

            if res > 0x7FFFFFFF: # or  if res > (2**31 -1):
                return 0

            x_remain //= 10

        return -res if x < 0 else res


if __name__ == '__main__':
    print(Solution().reverse(-12354))
    # MAX_INT = 2^31 - 1 = 2147483647
                         # 2147483651
    print(Solution().reverse(1563847412))
    print(Solution().reverse(1534236469)) # returns 0