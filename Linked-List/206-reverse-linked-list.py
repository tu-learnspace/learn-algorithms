"""
https://leetcode.com/problems/reverse-linked-list/

Kiểu gì để reverse list thì Time đều là O(N)
Tuy nhiên, Space thì có thể ối ưu từ O(N) xuống O(1) bằng cách dùng 2 biến để lưu trữ giá trị trước và sau

VD:
1 -> 2 -> 3 -> 4 -> 5
thì lúc duyệt 1 qua 2 thì mình trỏ lại
1 <- 2
và tiếp tục duyệt 2 qua 3
1 <- 2 <- 3
"""
# class ListNode(object):
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = ne = None

        while head:
            ne = prev
            prev = head
            head = head.next
            prev.next = ne
        return prev


if __name__ == '__main__':
