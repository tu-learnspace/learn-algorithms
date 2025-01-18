"""
https://leetcode.com/problems/reorder-list
Đề ======
Cho linked list: L0 -> L1 -> .. Ln-1 -> Ln
Reorder linked list thành: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Example:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Idea =========
1 -> 2 -> 3 -> 4 -> 5
Dùng fast slow pointer tìm middle, được 2 halves:
1 -> 2 -> 3
3 -> 4 -> 5

Reserve second half:
3 -> 4 -> 5 -> null to null <- 3 <- 4 <- 5

Combine:
1 -> 2 -> 3 -> null
   5 -> 4 -> 3 -> null

tmp1 = 2
tmp2 = 4
          f
1 -> 5 -> 2 -> 3 -> null
s
4 -> 3 ->

=> 1 -> 5 -> 2 -> 4 -> 3
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

        """
Combine:
1 -> 2 -> 3 -> null
   5 -> 4 -> 3 -> null

tmp1 = 2
tmp2 = 4
               f
1 -> 5 -> 2 -> 3 -> null
     s
4 -> 3 -> null

=> 1 -> 5 -> 2 -> 4 -> 3

        """
        fast, slow = head, prev
        print('zz', slow.val)
        while fast.next:
            print('====')
            tmp = fast.next
            print('tmp ', tmp.val)
            tmp2 = slow.next
            print('tmp2 ', tmp2.val)

            fast.next = slow
            slow.next = tmp

            fast = tmp
            slow = tmp2


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().reorderList(head)
    print('RESS')
    while head.next:
        print(head.val, end='-> ')
        head = head.next
