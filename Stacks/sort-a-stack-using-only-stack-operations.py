"""
== Đề
Given a stack, sort it using only stack operations (push and pop).

You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
The values in the stack are to be sorted in descending order, with the largest elements on top.


1. Input: [34, 3, 31, 98, 92, 23]
   Output: [3, 23, 31, 34, 92, 98]

2. Input: [4, 3, 2, 10, 12, 1, 5, 6]
   Output: [1, 2, 3, 4, 5, 6, 10, 12]

3. Input: [20, 10, -5, -1]
   Output: [-5, -1, 10, 20]

== Idea
Dùng 1 tmp_stack để sort, stack đó để track sorted element.
Pop element ra khỏi stack ban đầu đưa vào tmp_stack


"""
class Solution(object):
    def sortStack(self, s):
        res = []


        return res

if __name__ == '__main__':
    stack = [34, 3, 31, 98, 92, 23]
    res = Solution().sortStack(stack)
    print(res)