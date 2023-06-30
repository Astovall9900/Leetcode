class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for i, n in enumerate(seats):
            res += abs(n - students[i])
        return res
