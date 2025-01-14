"""
https://leetcode.com/problems/linked-list-cycle/
Đề ====
Cho linked list check nếu LL có vòng.

Idea =====
Cách 1:
- Dùng set để lưu trữ các node đã duyệt qua. Nếu node nào đã có trong set thì return True
- Time: O(N)
- Space: O(N)
Lưu ý: Đề bài không ràng buộc giá trị không bị lặp lại -> giá trị có thể bị lặp -> lưu cả node vào set luôn chứ ko chỉ node.value


Cách 2: Slow and Fast pointers
Định luật học thuộc: nếu có 2 racers chạy trong 1 vòng tròn, 1 racer nhanh hơn racer còn lại -> racer nhanh hơn chắc chắn
sẽ đuổi kịp & vượt qua racer chậm hơn từ phía sau. Nếu không có vòng thì racer nhanh hơn sẽ về đích (null) trước, còn có
vòng thì racer chậm sẽ gặp đc racer nhanh.
Lý giải dễ hiểu: vd cả 2 con trỏ đều vô vòng, liệu nó có gặp nhau được không?
Khi con trỏ nhanh approach con trỏ chậm từ đằng sau:
- Nếu con trỏ nhanh 1 bước chậm hơn: Thì step tiếp theo, con trỏ nhanh đi 2 bước, con trỏ chậm đi 1 bước -> gặp nhau.
- Nếu con trỏ nhanh 2 bước chậm hơn: Thì step tiếp theo, con trỏ nhanh sẽ chậm hơn con trỏ chậm 1 bước (quay về scenario 1)

-> Dùng 2 con trỏ, 1 con chạy nhanh, 1 con chạy chậm. Nếu 2 con trỏ gặp nhau thì return True
- Time: O(N)
- Space: O(1)

Giải thích về cách 2 (??):
p1 đi được a bước thì p2 đi được 2a bước. gọi x là số node của p1 đi đc trên vòng
rùa gặp thỏ: vị trí rùa = vị trí thỏ
=> a + x % b = a + (a + 2x) % b
=> x % b = (a + 2x) % b
=> (a + 2x - x) = k * b
=> a + x = k * b (k là số nguyên)
=> x = -a + kb (Chọn k nhỏ nhất cho x có nghĩa)
-> Rùa và thỏ gặp nhau tại tọa độ x
-> nếu tại vị trí đó mà đi thêm a bước nữa, rùa sẽ vào vị trí node bắt đầu của cycle
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __bool__(self):
        return self.next is not None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # C1: use set
        # seen = set()
        #
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        #
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