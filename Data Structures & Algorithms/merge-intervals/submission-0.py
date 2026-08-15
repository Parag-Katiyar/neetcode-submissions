class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        array = [intervals[0]]
        i = 1
        j = 0 

        while i < len(intervals):

            if intervals[i][0] <= array[j][1]:

                array[j] = [array[j][0], max(array[j][1], intervals[i][1])]
                i = i + 1 
            else:
                array.append(intervals[i])
                i = i + 1
                j = j+1
                
            
        return array


        