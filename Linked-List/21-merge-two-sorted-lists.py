"""
https://leetcode.com/problems/merge-two-sorted-lists

3 điều rút ra:
- Không edit gì trên 2 list hết, dùng 1 node_ảo để trỏ
- Dùng 1 node_ảo ban đầu: res = node_ảo. Rồi cho node_ảo chạy thôi
- 1 trong 2 list có thể sẽ hết trước, lúc này chỉ cần append list còn lại vô kết quả (vì list đã đc sorted)
"""

# ================== LeetCode answer ==================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 or list2

        res = tmp = ListNode(float("inf"))

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        tmp.next = list1 or list2

        return res.next  # bỏ đi cái "inf" ở đầu


# ========================= My Solution (based on my DS implementation) =========================
from index import LinkedList as ListNode
from index import Node

class MySolution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1.head or not list2.head:
            return list1 or list2

        node1 = list1.head
        node2 = list2.head
        res = ListNode()
        tmp = Node(float("inf"))

        has_run_once = False

        while node1 and node2:
            if node1.val < node2.val:
                tmp.next = node1
                node1 = node1.next
            else:
                tmp.next = node2
                node2 = node2.next

            # if này chỉ dùng để loại cái node "inf" ở đầu thôi, nếu không thì dùng deleteAtBeginning() lúc return res cũng được
            if not has_run_once:
                has_run_once = True
                res.head = tmp.next

            tmp = tmp.next

        #
        tmp.next = node1 or node2
        return res


if __name__ == '__main__':
    list1 = ListNode()
    list2 = ListNode()

    # Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    # Output: [1, 1, 2, 3, 4, 4]
    list1.insertAtEnd(1)
    list1.insertAtEnd(2)
    list1.insertAtEnd(4)
    list1.printList()
    list2.insertAtEnd(1)
    list2.insertAtEnd(3)
    list2.insertAtEnd(4)
    list2.printList()

    # Input: list1 = [], list2 = [0]
    # Output: [0]
    # list2.insertAtEnd(0)

    res = MySolution().mergeTwoLists(list1, list2)
    res.printList()
