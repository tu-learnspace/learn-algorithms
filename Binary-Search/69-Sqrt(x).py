"""
https://leetcode.com/problems/sqrtx

Căn x sẽ nhỏ hơn x/2 (trong khúc x -> x/2)
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x    # sqrt(0) = 0, sqrt(1) = 1

        left, right = 2, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = mid * mid

            if sqrt > x:
                right = mid - 1
            elif sqrt < x:
                left = mid + 1
            else:
                return mid
        # đề kêu làm tròn lên
        return right

if __name__ == '__main__':
    #x = 8
    x = 6
    res = Solution().mySqrt(x)
    print(res)