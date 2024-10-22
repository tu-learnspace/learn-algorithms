"""
https://leetcode.com/problems/linked-list-cycle/

Cách 1:
- Dùng set để lưu trữ các node đã duyệt qua. Nếu node nào đã có trong set thì return True
- Time: O(N)
- Space: O(N)
Lưu ý: Đề bài không ràng buộc giá trị không bị lặp lại -> giá trị có thể bị lặp -> lưu cả node vào set luôn chứ ko chỉ node.value


Cách 2: Slow and Fast pointers
Dùng 2 con trỏ, 1 con chạy nhanh, 1 con chạy chậm. Nếu 2 con trỏ gặp nhau thì return True
- Time: O(N)
- Space: O(1)

Giải thích về cách 2:
- Nếu có cycle thì con trỏ chạy nhanh sẽ gặp con trỏ chạy chậm
- Nếu không có cycle thì con trỏ chạy nhanh sẽ gặp null trước con trỏ chạy chậm


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
        # tmp = set()
        #
        # while head:
        #     if head in tmp:
        #         return True
        #     tmp.add(head)
        #     head = head.next
        #
        # return False

        # C2: use 2 pointers
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


