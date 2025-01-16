"""
https://leetcode.com/problems/linked-list-cycle-ii
Đề =====
Cho linked list có vòng, tìm điểm bắt đầu Linked list.

Idea =====
C1 đơn giản là lưu các node trong hash map. Node nào mà lặp lại thì đó là start của cycle -> Ko tối ưu về space.

C2: dựa vào bài Linked List Cycle để tính độ dài vòng. Giả sử là K.
Tính xong thì init lại slow ở chỗ bắt đầu, fast ở K node ahead slow -> khi fast & slow gặp nhau sẽ là start cycle.
Giải thích: giả sử slow đến start cycle rồi thì lúc đó fast đang K node ahead slow, which is ở start cycle luôn (vì K là
độ dài cycle).

C3: Floyd’s Tortoise and Hare algorithm
Học thuộc: sau khi detect vòng xong thì reset slow về vị trí bắt đầu, lúc này slow & fast tếp tục move 1 node. Khi gặp nhau,
chỗ đó là start of cycle.

Chứng minh: p1 đi được a bước thì p2 đi được 2a bước.
gọi x là số node của p1 đi đc trên vòng. a là quãng đường để tới vòng.
rùa gặp thỏ: vị trí rùa = vị trí thỏ
=> a + x % b = a + (a + 2x) % b  // modulo để ra vị trí trong vòng
=> x % b = (a + 2x) % b
=> (a + 2x - x) = k * b
=> a + x = k * b (k là số nguyên)
=> x = -a + kb
-> Rùa và thỏ gặp nhau tại tọa độ x
-> Chọn k nhỏ nhất cho x có nghĩa -> Nếu tại vị trí đó mà đi thêm a bước nữa, rùa sẽ vào vị trí node bắt đầu của cycle
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # C3: Floyd’s Tortoise and Hare algorithm
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # No cycle is found
        if fast is None or fast.next is None:
            return None

        while head != slow:
            head = head.next
            slow = slow.next
        return head

if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next = head.next
    res = Solution().detectCycle(head)
    print(res.val)