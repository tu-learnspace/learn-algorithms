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

"""
class Solution(object):
    def canAttendAllAppointments(self, intervals):
        return False


if __name__ == '__main__':
