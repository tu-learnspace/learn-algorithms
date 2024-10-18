"""
https://leetcode.com/problems/merge-two-sorted-lists

3 điều rút ra:
- Dùng 1 node_ảo ban đầu: res = node_ảo. Rồi cho node_ảo chạy thôi
    - Có thể hơi confuse tạo sao res là kết quả được -> res nó chỉ là "đường vào" (ban đầu trỏ vô node_ảo)
    - Không thể dùng lại list1/list2/node_ảo hết vì cho tụi nó trỏ tùm lum rồi (đến cuối cùng nó trỏ vô null/trỏ vô ptử cuối) -> lí do node_ảo sinh ra, là để thế mạng cho res
- 1 trong 2 list có thể sẽ hết trước, lúc này chỉ cần append list còn lại vô kết quả (vì list đã đc sorted)

Mẹo rút ra (general luôn):
- if not list1 or not list2: return list1 or list2: nếu 1 trong 2 thằng null thì return thằng còn lại ko null, đỡ phải 2 vòng if
"""

# ================== LeetCode answer (based on LC simple LL implementation below) ==================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Time: O(n + m) (n, m là số node của list1, list2)
    Space: O(1) (không dùng thêm gì ngoài tmp)
    """
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


# ========================= My Solution (based on my DS implementation in index.py) =========================
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

