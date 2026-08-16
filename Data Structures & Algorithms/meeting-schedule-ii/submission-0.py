"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # Extract start and end times using the Interval object attributes
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        count = 0
        countx = 0 
        l = len(intervals)
        i = 0
        j = 0 

        while i < l: 
            if start[i] < end[j]: 
                count = count + 1
                i = i + 1 
            elif end[j] <= start[i]:
                count = count - 1
                j = j + 1 
            countx = max(countx, count)
        
        return countx