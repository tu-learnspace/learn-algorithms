"""
https://leetcode.com/problems/middle-of-the-linked-list
Đề =====
Tìm phẩn tử ở giữa LL, nếu có 2 node ở giữ thì return cái phía sau

Idea ======
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)

    res = Solution().middleNode(head)
    print(res.val)