class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        last = self.head

        # Otherwise, traverse the list to find the last node
        while last.next:
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()  # Ensures the output is followed by a new line


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

class Solution(object):
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
