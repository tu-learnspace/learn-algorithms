"""
https://leetcode.com/problems/meeting-rooms
Đề ========
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Appointments: [[6,7], [2,4], [13, 14], [8,12], [45, 47]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Idea ====
Sort theo start rồi so sánh [i+1].start < i.end là có conflict
"""
class Solution(object):
    def canAttendAllAppointments(self, intervals):
        intervals.sort(key = lambda x: x[0])

        for i in range(len(intervals) - 1):
            if intervals[i + 1][0]  < intervals[i][1]:
                return False
        return True

if __name__ == '__main__':
    appointments = [[6, 7], [2, 4], [13, 14], [8, 12], [45, 47]]
    # appointments = [[1,4], [2,5], [7,9]]
    res = Solution().canAttendAllAppointments(appointments)
    print(res)