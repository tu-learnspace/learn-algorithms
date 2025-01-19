"""
https://leetcode.com/problems/reorder-list
Đề ======
Cho linked list: L0 -> L1 -> .. Ln-1 -> Ln
Reorder linked list thành: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Example:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Idea =========
Dùng fast slow pointer tìm middle, được 2 halves:
1 -> 2 -> 3 -> 4 -> 5
          s

Reserve second half:
1 -> 2 -> 3 <- 4 <- 5
          |
         null
Combine:
f
1 -> 2 -> 3 -> null
   4 -> 5 -> 3 -> null
   s
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        # find middle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # combine
        fast, slow = head, prev
        while slow.next:
            # temp var for moving next
            next_fast = fast.next
            next_slow = slow.next
            # swap
            fast.next = slow
            slow.next = next_fast
            # moving next
            fast = next_fast
            slow = next_slow



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().reorderList(head)
    while head:
        print(head.val, end=' -> ')
        head = head.next
