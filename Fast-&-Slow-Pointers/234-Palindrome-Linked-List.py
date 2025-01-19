"""
https://leetcode.com/problems/palindrome-linked-list
Đề ====
Check xem linked list có phải là palindrome k (đọc forward và backward như nhau)
Input: head = [1,2,3,2,1]
Output: true

Idea ====
Từ điểm ở giữa đi về 2 đầu sẽ giống nhau. -> Tìm điểm ở giữa bằng fast slow
Đứng từ đó, reverse nửa sau (để duyệt)
Sau khi reverse nửa sau xong, bắt đầu duyệt 2 nửa xem có giống nhau ko, giống thì return True.
VD:
1. Dùng fast, slow. Khi này fast ở cuối, slow ở middle.
1 -> 2 -> 3 -> 2 -> 1
          s
2. Reverse nửa sau 3 -> 2 -> 1 -> null thành null <- 3 <- 2 <-1. Cứ move slow đi, dùng 1 biến temp để giữ lại vị trí next để point tiếp
null <- 3 -> 2 -> 1 -> null
prev    s   tmp

tmp = s.next
s.next = prev
prev = s
s = tmp

3. Compare 2 nửa
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # 1. find middle.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half.
        prev = None # prev to keep the old position of slow for it to point back
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # 3. check 2 part if they are equal.
        slow = prev # slow cuối cùng bị move vô null rồi nên phải lấy prev
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    res = Solution().isPalindrome(head)
    print(res)