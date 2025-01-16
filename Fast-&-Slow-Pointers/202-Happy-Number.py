"""
https://leetcode.com/problems/happy-number/
Đề ====
Cho 1 số, check xem có phải là happy number ko. Happy number là số mà sum của các digit^2 lên cuối cùng bằng 1.
Nếu nó ko end bằng 1 thì nó sẽ lặp endlessly in cycle.
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Input: 12
Output: false (12 is not a happy number)
Explanations:
1^2 + 2^2 = 5
5^2 = 25
2^2 + 5^2 = 29
2^2 + 9^2 = 85
8^2 + 5^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
Please note the cycle from 89 -> 89 (Nếu ko end đc bằng 1 thì sẽ lặp trong loop hoài).

Idea ====
C1: Nếu lặp trong loop thì k phải happy number -> Dùng hash lưu lại sum của các lần. Nếu lặp lại trong hash -> loop. Nếu
end bằng 1 thì sẽ kết thúc while.

C2: Như bài linked list cycle:
- Nếu là happy number thì lặp trong cycle của toàn số 1.
- Nếu k là happy number thì lặp trong cycle của 1 dãy số nào đó.

Tips: Để tách digit của 1 số thì dùng div // để lấy n còn lại sau khi chia lấy digit và mod % để lấy digit.
Có thể dùng luôn hàm built in divmod -> trả về 2 giá trị: phần nguyên và phần dư
VD: divmod(10, 3) = <3, 1> (10 // 3 = 3, 10 % 3 = 1)
"""
class Solution(object):
    def square_sum(self, n):
        total_sum = 0
        while n > 0:
            # n, digit = divmod(n, 10)
            digit = n % 10
            total_sum += digit * digit
            n //= 10
        return total_sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # C1: dùng set
        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = self.square_sum(n)
        # return n == 1

        # C2: dùng fast, slow pointer
        slow = fast = n
        while True:
            slow = self.square_sum(slow)  # move one step
            fast = self.square_sum(self.square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
                break
        return slow == 1


if __name__ == '__main__':
    print(Solution().isHappy(19))