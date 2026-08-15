#Two important Base cases !
#Changing the Length of the List !
#max condition 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Insert at right position 
        #Then Combine
        l = len(intervals)
        inserted = False
        

        for i in range (0,l):

            if i ==0: 
                if intervals[0][0] > newInterval[0]:
                    intervals.insert(0, newInterval)
                    inserted = True  
                    break
            
            if intervals[i][0] >= newInterval[0]: 

                intervals.insert(i, newInterval)
                break 
     
        if inserted == False: 
            intervals.append(newInterval)
        
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
















