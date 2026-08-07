class Solution:
    def numDecodings(self, s: str) -> int:

        l = len(s)

        memo = {}

        def num(i): 


            if i in memo: 
                return memo[i]


            if i >= l: 
                return 1 #Needed correction 

            if int(s[i]) == 0: 
                return 0 

            if int(s[i]) == 1 and i <=l-2:
                n_i = num(i+1) + num(i+2)
                
            if int(s[i]) == 1 and i == l-1:
                return 1

            if i <= l-2 and int(s[i]) == 2 and int(s[i+1]) < 7:
                n_i = num(i+1) + num(i+2)

            if i <= l-2 and int(s[i]) == 2 and int(s[i+1]) >= 7: 
                n_i = num(i+1) 

            if i == l-1 and int(s[i]) == 2:
                n_i = num(i+1)
            
            if int(s[i]) > 2: 
                n_i = num(i+1) #needed corection

            memo[i] = n_i
            return n_i

        return num(0)




        
#No need to map just conditions