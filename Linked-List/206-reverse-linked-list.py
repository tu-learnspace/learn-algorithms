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
from index import LinkedList

class Solution(object):
    """
    Time: O(N)
    Space: O(1)
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = tmp = None

        while head:
            tmp = prev
            prev = head
            head = head.next
            prev.next = tmp

        return prev


if __name__ == '__main__':
    llist = LinkedList()
    # [1, 2, 3, 4, 5]
    llist.insertAtBeginning(5)
    llist.insertAtBeginning(4)
    llist.insertAtBeginning(3)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(1)

    # [1, 2]
    # llist.insertAtBeginning(2)
    # llist.insertAtBeginning(1)

    # []

    llist.printList()

    llist.head = Solution().reverseList(llist.head)
    llist.printList()
