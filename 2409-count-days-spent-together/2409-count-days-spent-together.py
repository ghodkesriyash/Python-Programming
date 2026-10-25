class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = {
            1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
            7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334
        }
        def convert(date):
            return days[int(date[:2])] + int(date[3:])

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        return max(0, end - start + 1) 
        