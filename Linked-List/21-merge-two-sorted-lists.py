"""
https://leetcode.com/problems/merge-two-sorted-lists


"""
from index import LinkedList

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1.head:
            return list2
        if not list2.head:
            return list1

        while list1.head < list2.head:



if __name__ == '__main__':
    list1 = LinkedList()
    list2 = LinkedList()

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

    res = Solution().mergeTwoLists(list1, list2)
    res.printList()

