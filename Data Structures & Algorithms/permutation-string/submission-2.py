class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
    
    # Frequency map for s1
        mp = {}
        for i in range(len(s1)):
            if s1[i] not in mp:
                mp[s1[i]] = 1 
                continue 
            if s1[i] in mp: 
                mp[s1[i]] = mp[s1[i]] + 1
        
    # Slide across s2
        for i in range(len(s2)):
        # Only start checking when we have a full window of size len(s1)
            if i >= len(s1) - 1:
                hs = {}
                for j in range(i - len(s1) + 1, i + 1):
                    if s2[j] not in hs:
                        hs[s2[j]] = 1 
                        continue

                    if s2[j] in hs: 
                        hs[s2[j]] = hs[s2[j]] + 1
            
                if hs == mp: 
                    return True 

        return False













