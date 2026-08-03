def rep(node,word,index):

    if index == len(word):
        return node.end

    if word[index]==".": 
        for ch in node.children: 
            if rep(node.children[ch],word,index+1): 
                return True
            
    elif word[index] in node.children: 
        if rep(node.children[word[index]],word,index+1): 
            return True
    
    return False
    



    

    
     
     

class tnode:
    def __init__(self):
        self.children = {}
        self.end = False          
        

class WordDictionary:
    def __init__(self):
        self.root = tnode()
        

    def addWord(self, word: str) -> None:

        node = self.root
        for w in word:
            if w not in node.children: 
                node.children[w] = tnode()  # Fixed: Changed tnode() to TrieNode()
            node = node.children[w]
        node.end = True
        
        

    def search(self, word: str) -> bool:

        node = self.root
        return rep(node,word,0)

        


