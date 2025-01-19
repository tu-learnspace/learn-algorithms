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

Chỉ chứng minh được bằng toán học: khi fast & slow gặp nhau ở trong vòng (fast đã đi hết vài vòng).
Gọi a là số bước cần đi tới vòng, b là số bước trong vòng tới điểm gặp nhau.
Vì slow đi được a bước thì fast đi được 2a bước. Gọi x là quãng đường của fast đi đc trên vòng. a là quãng đường để tới vòng.
Fast gặp slow: vị trí fast = vị trí slow
=> a + x % b = a + (a + 2x) % b  // modulo để ra vị trí trong vòng, ko modulo a vì lúc đó chưa vô vòng
=> x % b = (a + 2x) % b
=> (a + 2x - x) = k * b
=> a + x = kb (k là số nguyên)
=> x = -a + kb
=> x = -a (Chọn k nhỏ nhất cho x có nghĩa)
-> Nghĩa là lần gặp gần nhất tiếp theo sẽ ở vị trí đó mà đi thêm a bước nữa. Mà a lại bằng khoảng cách từ head tới vòng luôn.
-> Cho nên sau khi detect điểm gặp nhau, ta cho head đi tiếp (slow cũng đi) cho đến khi gặp nhau (ensure đc vị trí đó ở đầu vòng luôn).
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
        # C2
        # cycle_len = 0
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast: # cycle detected
        #         curr = slow
        #         while True: # calculate the cycle length by đi 1 vòng
        #             curr = curr.next
        #             cycle_len += 1
        #             if curr == slow:
        #                 break
        #         break
        # # Handle edge case: No cycle is found
        # if fast is None or fast.next is None:
        #     return None
        # # Reset to start
        # slow = fast = head
        # # Move fast cycle_len node ahead slow
        # while cycle_len > 0:
        #     fast = fast.next
        #     cycle_len -= 1
        #
        # while fast != slow:
        #     fast = fast.next
        #     slow = slow.next
        # return slow

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