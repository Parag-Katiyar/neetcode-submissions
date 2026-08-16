#Why using max fro updating the track is redundant --> if we enounter such eleemnts that have very large span then it will imediately collapse no need to go to the thirs element an compare.

"ok that is why in the question minimum nuber of intervals which are to be removed we only see the only tow overallapping current intervals and we don't worry about next to next intervals if we remove the max end then form the this logic ir is the safest option we can do and this ligic makes it robus choice that what needed in greedy"
"""
"no yesterday i was solivi it but was worries abiut the future inrterval overlapping I saw the solution but was loooking like a guess not lofical robust but tday iused max (which basically repeeated my ideas) that got refined and I got the logic of the min non overlapping intervals"

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # Compare current start with previous end
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
                
        return True









