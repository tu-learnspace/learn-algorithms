"""
https://leetcode.com/problems/powx-n/description/
Tính x^n

Tối ưu bằng cách mỗi lần nhân thì get more work done → giảm số lần nhân nhưng vẫn giữ kết quả đúng.
Số phép nhân tối ưu nhất thì cũng phải là 1 lần. (do vd tính x^6 thì k thể nói x^6 = x^6 đc, lẹ nhất là: 2 thằng x^3 nhân nhau)
x^6 = (x^3)^2 = x^3 * x^3 → nếu tính x^3 thì chỉ cần 1 phép nhân
x^3 = x^2 * x → chỉ cần 1 phép nhân
x^2 = x * x


  9^6                              X^N
= 9^3 x 9^3                        X^N x X^N (N = N/2, N là số chẵn)
= (9^2 x 9) x (9^2 x 9)            X^N x X^N x X (N = N/2, N là số lẻ)
= ((9 x 9) x 9) x ((9 x 9) x 9)
"""
class Solution:
    def myPow(self, x, n):
        """
        - nếu n lẻ thì x^n = x^(n//2) * x^(n//2) * x
        - nếu n chẵn thì x^n = x^(n//2) * x^(n//2)
        """
        res = 1.0

        # nếu n < 0 thì x^-n = 1/x^n
        if n < 0:
            n, x = -n, 1.0 / x
        while n:
            if n & 1:  # n lẻ
                res *= x
            x, n = x*x, n >> 1 # chia 2
        return res


if __name__ == '__main__':
    print(Solution().myPow(2, 4))