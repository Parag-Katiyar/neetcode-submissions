import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        mapx = {}
        for i in times: 
            if i[0] not in mapx: 
                mapx[i[0]] = []
            mapx[i[0]].append([i[1],i[2]])

        heap_one = []
        time = {}

        time[k] = 0
        heapq.heappush(heap_one, (0,k))

        while heap_one: 

            time_curr,x = heapq.heappop(heap_one)

            # Skip stale heap entry: a better time to reach x is already known
            if time_curr > time[x]:
                continue
                
            # Relaxing and pushing
            for i in mapx.get(x,[]):

                if i[0] not in time: 
                    time[i[0]] =  i[1] + time_curr
                    heapq.heappush(heap_one,(time[i[0]], i[0]))


                else: 
                    if i[1] + time_curr < time[i[0]]: 

                        time[i[0]] =  i[1] + time_curr

                        heapq.heappush(heap_one,(time[i[0]], i[0]))

        if len(time) < n: 
            return -1
        else: 
            return max(time.values())











            