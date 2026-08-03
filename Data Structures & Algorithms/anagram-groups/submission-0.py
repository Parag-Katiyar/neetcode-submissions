class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-97] = arr[ord(j)-97] + 1
            d[tuple(arr)].append(i)
        
        return(list(d.values()))
        


        