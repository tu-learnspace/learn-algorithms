"""
== Đề
Given a stack, sort it using only stack operations (push and pop).
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
The values in the stack are to be sorted in descending order, with the largest elements on top.

Input: [34, 3, 31, 98, 92, 23]
Output: [3, 23, 31, 34, 92, 98]

Input: [20, 10, -5, -1]
Output: [-5, -1, 10, 20]

== Idea
Dùng 1 temp stack để sort, stack đó để track sorted element. Việc sort có thể được done bằng cách liên tục pop element ra
khỏi input stack rồi push vào temp stack theo thứ tự, cần rearrange element tới khi input stack empty.

VD: [34, 3, 31, 98, 92, 23]

Pop từ main stack (đi từ cuối) sang temp stack.
[34, 3, 31, 98, 92] [23]

[34, 3, 31, 98] [23, 92]

[34, 3, 31] [23, 92, 98]

[34, 3] 31 [23, 92, 98]
31 pop ra nhưng check thấy ko lớn hơn 98 nên ko push vô tiếp nữa

[34, 3, 98, 92] 31 [23]
mà phải pop temp stack ra tới 23 rồi mới push vô được

[34, 3, 98, 92] [23, 31]
xong rồi mới đưa 31 vô

cuối cùng pop 98, 92 rồi push quay lại temp stack
[34, 3]  [23, 31, 92, 98]

tiếp tục làm tương tự

"""
class Solution(object):
    def sortStack(self, s):
        """
        VD: [34, 3, 31, 98, 92, 23]

        """

        temp_stack = []

        while s:
            temp = s.pop()


        return temp_stack

if __name__ == '__main__':
    stack = [34, 3, 31, 98, 92, 23]
    res = Solution().sortStack(stack)
    print(res)