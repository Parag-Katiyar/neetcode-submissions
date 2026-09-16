######### IMPORTANT ----->   Do I need to compare every pair of words, or only neighboring words? No you do not yes by doing this you will get a elaborate edges but only by comparing the neighbours yuo will get sufficient information. and comapring all will also boil down to the same conditions ########################

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
     
        edges = set()
        l = len(words)

        for i in range(0,l-1): 
            x = 0 

            l1 = len(words[i])
            l2 = len(words[i+1])

            while x < l1 and x < l2 and words[i][x] == words[i+1][x]:
                x = x + 1

            if x == l2 and l1 > l2:
                return ""

            if x < l1 and x < l2:
                if (words[i][x], words[i+1][x]) not in edges:
                    edges.add((words[i][x], words[i+1][x]))
            #Wisdom note
            #When traversing two sequences simultaneously: bounds first, then compare/process.
            #The point where the loop stops can itself be the answer/information.

            #Counting number of different Alphabets
        all_alpha = set()
           
        for i in words:

            l = len(i)

            for j in range(0,l): 
                all_alpha.add(i[j])
                
        count = len(all_alpha)

            #adjenmcy_map ..out going vectors
        out_going = {}
        in_coming = {}

        for i in all_alpha: 

            out_going[i] = []
            in_coming[i] = 0 

        for j in edges: 

            out_going[j[0]].append(j[1])
            in_coming[j[1]] = in_coming[j[1]] + 1

        que = deque()
        result = []

        x = 0

        for i in in_coming: 
            if in_coming[i] == 0:
                que.append(i)
                x = x + 1

        while que:

            node = que.popleft()
            result.append(node)
                

            for i in out_going[node]: 

                if in_coming[i] != 0:
                    in_coming[i] = in_coming[i] - 1

                if in_coming[i] == 0: 
                    que.append(i)
                    x = x + 1
                        
        if x != count: 
            return ""
        if x == count: 
            return "".join(result)
                 
                
                

            
            
            
                
                    

        
        








