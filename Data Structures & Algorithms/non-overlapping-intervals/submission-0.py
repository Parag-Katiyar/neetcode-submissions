class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        #Track the end of the intervals whenver you encounter the overlpa choose the interval with min end
        count = 0
        track = intervals[0][1] 
        l = len(intervals)

        for i in range(1,l):

            if intervals[i][0] < track: 
                count = count + 1 
                track = min(intervals[i][1],track)
            else: 
                track = intervals[i][1]
        
        return count 



        