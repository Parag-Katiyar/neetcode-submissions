class tnode:
    def __init__(self):
        self.children = {}
        self.branch_end = False  
        self.word_end = False    

def addWord(root, word: str) -> None:

        node = root

        for i in range(0, len(word)):

            if word[i] not in node.children:
                node.children[word[i]] = tnode()

            node = node.children[word[i]]

            if i != len(word) - 1 and node.branch_end == True:
                node.branch_end = False

            if i == len(word) - 1:
                node.word_end = True

        if not node.children:
            node.branch_end = True 


        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        root = tnode()
        l = len(s)
        memo = {} 

        for w in wordDict: 
            addWord(root,w)
        
        def search(index):

            if index == l: 
                return True

            if index in memo: 
                return memo[index]

            node = root
            x = False
            
            
            for i in range(index,l):

                if s[i] not in node.children:
                    break  

                node = node.children[s[i]]

                if node.word_end: 
                    if search(i+1):
                        memo[index] = True 
                        return True 
                    
            memo[index] = False    
            return False 
        

        return search(0)


        

    


    

        