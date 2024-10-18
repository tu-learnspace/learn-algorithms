"""
https://leetcode.com/problems/linked-list-cycle/

Cách 1:
- Dùng set để lưu trữ các node đã duyệt qua. Nếu node nào đã có trong set thì return True
- Time: O(N)
- Space: O(N)
Lưu ý: Đề bài không ràng buộc giá trị không bị lặp lại -> giá trị có thể bị lặp -> lưu cả node vào set luôn chứ ko chỉ node.value


Cách 2:

"""

# ================== LeetCode answer (based on LC simple LL implementation below) ==================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # C1: use set
        tmp = set()

        while head:
            if head in tmp:
                return True
            tmp.add(head)
            head = head.next

        return False

