"""
https://leetcode.com/problems/number-of-1-bits/
Đếm số set bit của 1 so

Công thức thuộc lòng: x & (x - 1) → xóa bit 1 thấp nhất của x (clear the rightmost set bit)
→ Áp dụng bài này clear bit 1 tới khi hết bit 1 luôn (mean = 0)
"""

def hammingWeight(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

if __name__ == '__main__':
    # 11 = (1011) -> 3
    print(hammingWeight(11))