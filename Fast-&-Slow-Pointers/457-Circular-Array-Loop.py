"""
https://leetcode.com/problems/circular-array-loop
Đề =====
Cho array, tại i thì arr[i] là số bước phải đi tiếp (dương tiến tới, âm lùi lại). Assume việc di chuyển là circular (tới cuối
thì vòng về đầu & ngc lại). Check xem array có cycle không:
- Cycle phải có ít nhất 1 element.
- Cycle chỉ được đi 1 hướng.
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0. Hướng đi chỉ có 1 hướng tiến tới.

Input: [2, 1, -1, -2]
Output: false
Explanation: Mặc dù có vẻ có cycle ở 1, 2 nhưng vì đi 2 hướng tới & lùi nên ko tính.

Input: nums = [1,-1,5,1,4]
Output: true
Explanation: có 3 cycle ở đây:
- cycle 0,1 thì bị 2 hướng
- cycle 2 thì chỉ có 1 element là nó (5 move 5 bước cũng ra 5)
- cycle 3 -> 4 -> 3: valid

Idea ======
Ở vd 3, cycle có thể ở bất cứ element nào -> phải duyệt all, mỗi element check for cycle.
- Khi array là circular thì để tìm index thì dùng modulo.
- Để check cycle thì dùng fast, slow pointer: fast sẽ nhảy 2 lần, slow nhảy 1 lần.
- Để check cycle đó ko bị 2 hướng thì tất cả các số phải cùng dương/âm -> dùng 1 biến store direction tại i để check,
nếu khác chiều break ngay.
- Để check cycle phải có hơn 1 element: nếu next element là the same current thì break luôn.

Optimize: cách trên thì với mỗi nums[i] sẽ duyệt mọi node khác để tìm vòng -> O(N^2)
Nhận xét: nếu 1 node đã đc duyệt qua (visited) mà nó ko trả về kết quả có vòng, thì có nghĩa nếu lần sau giả sử có đi vô
cái node đó thì cũng sẽ ko thể nào có vòng (sẽ đi same path).
-> Dùng 1 mảng visited để check element đó đã đi qua chưa, nếu rồi thì skip trong mỗi lần duyệt i tiếp theo. Node đã đc duyệt sẽ ko bị duyệt lại.
-> Time: O(N) (nhưng space từ O(1) thành O(N))
"""
class Solution(object):
    # Return next position. If not qualified, return -1
    def findNextIndex(self, arr, curr_pos, is_forward):
        curr_direction = arr[curr_pos] >= 0

        if is_forward != curr_direction:  # Các next step ko cùng hướng với nums[i]
            return -1

        next_pos = (curr_pos + arr[curr_pos]) % len(arr)

        if next_pos == curr_pos: # Cycle 1 element
            return -1
        return next_pos

    # For optimization: mark all elements of a fully traversed path to skip them in future iterations
    def markVisited(self, arr, i, is_forward, visited):
        curr_pos = i
        while True:
            visited[curr_pos] = True
            next_pos = self.findNextIndex(arr, curr_pos, is_forward)
            if next_pos == - 1 or visited[next_pos]:
                break
            curr_pos = next_pos

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            fast, slow = i, i
            is_forward = nums[i] >= 0
            while True:
                slow = self.findNextIndex(nums, slow, is_forward)
                fast = self.findNextIndex(nums, fast, is_forward)
                if fast != -1:
                    fast = self.findNextIndex(nums, fast, is_forward)

                if slow == -1 or fast == -1:
                    break # break chứ ko có return để check phía sau biết đâu còn
                if slow == fast:
                    return True

            # Mark visited cho mọi element trong path từ nums[i]
            # Note: phải mark sau khi duyệt path xong xuôi (chứ đang duyệt mà mark thì interrupt sao)
            self.markVisited(nums, i, is_forward, visited)

        return False

if __name__ == '__main__':
    # arr = [1, 2, -1, 2, 2]
    # arr = [2, 1, -1, -2]
    # arr = [1, -1, 5, 1, 4]
    arr = [-1, -2, -3, -4, -5, 6]
    res = Solution().circularArrayLoop(arr)
    print(res)