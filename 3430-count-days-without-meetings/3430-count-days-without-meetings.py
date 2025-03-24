class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        for i in range(len(meetings) - 1):
            if meetings[i][1] >= meetings[i+1][0]:
                meetings[i+1][0] = meetings[i][0]
                meetings[i+1][1] = max(meetings[i][1], meetings[i+1][1])
            else:
                days -= meetings[i][1] - meetings[i][0] + 1
        return days - (meetings[-1][1] - meetings[-1][0] + 1)