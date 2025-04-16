"""
https://leetcode.com/problems/convert-to-base-2
Đề ====
Convert thành base -2

Input: n = 2
Output: "110"
Explantion: (-2)^2 + (-2)^1 = 2

Input: n = 3
Output: "111"
Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3

Idea ====
Quy đổi decimal sang binary thì ta chia n cho 2 (tới khi n = 0) rồi lưu remainder (số dư) lại. Remainder khi chia 2 có
thể là 1 hoặc 0:
- n % 2 -> dùng n & 1 (extract last bit, 1 or 0)
- n / 2 -> dùng n >>= 1
Tuy nhiên, với số âm thì khi chia âm, remainder có thể bị âm (k đc vì remainder chỉ đc là 0 hoặc 1) -> enforce remainder
là dương, thì số bị âm là số bị chia (n) -> thêm âm khi n/2: n = - (n << 1)
"""
class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        stack = []
        while n:
            stack.append(n & 1) # remainder (& 000..001 -> loại hết trừ thằng bit cuối)
            n = -(n >> 1) # divided by -2
        return ''.join(str(i) for i in reversed(stack))

if __name__ == '__main__':
    num = 3
    res = Solution().baseNeg2(num)
    print(res)