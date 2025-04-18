"""
https://leetcode.com/problems/linked-list-cycle/
Đề ====
Cho linked list, check nếu LL có vòng.

Idea =====
Cách 1:
- Dùng set để lưu trữ các node đã duyệt qua. Nếu node nào đã có trong set thì return True
- Time: O(N)
- Space: O(N)
Lưu ý: Đề bài không ràng buộc giá trị không bị lặp lại -> giá trị có thể bị lặp -> lưu cả node vào set luôn chứ ko chỉ node.value

Cách 2: Slow and Fast pointers
Định luật học thuộc: nếu có 2 racers chạy trong 1 vòng tròn, 1 racer nhanh hơn racer còn lại -> racer nhanh hơn chắc chắn
sẽ đuổi kịp & vượt qua racer chậm hơn từ phía sau. Nếu không có vòng thì racer nhanh hơn sẽ về đích (null) trước, còn có
vòng thì racer chậm sẽ gặp đc racer nhanh trong vòng.
Lý giải dễ hiểu: vd cả 2 con trỏ đều vô vòng, liệu nó có gặp nhau được không?
Khi con trỏ nhanh approach con trỏ chậm từ đằng sau:
- Nếu con trỏ nhanh 1 bước chậm hơn: Thì step tiếp theo, con trỏ nhanh đi 2 bước, con trỏ chậm đi 1 bước -> gặp nhau.
- Nếu con trỏ nhanh 2 bước chậm hơn: Thì step tiếp theo, con trỏ nhanh sẽ chậm hơn con trỏ chậm 1 bước (quay về scenario 1)
-> Dùng 2 con trỏ, 1 con chạy nhanh, 1 con chạy chậm. Nếu 2 con trỏ gặp nhau thì return True
- Time: O(N)
- Space: O(1)

Q: Con trỏ fast bắt buộc phải fast gấp đôi con trỏ slow?
A: Đúng vì nếu giả sử gấp 3 thì có TH fast luôn hơn chậm 1 node & ko gặp nhau đc. Vì slow move 1, fast move 2 thì ở POV
của slow thì slow đứng yên & fast move 1 -> eventually sẽ fast sẽ reach slow.
Còn nếu slow move 1, fast move 3 thì POV của slow là slow đứng yên & fast move 2 -> ko guarantee đc fast sẽ gặp slow.
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # C1: use set
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False

        # C2: use 2 pointers
        fast = slow = head
        while fast and fast.next: # while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

if __name__ == '__main__':
    # head = [3,2,0,-4], pos = 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    res = Solution().hasCycle(head)
    print(res)