def rep(node,word,index):

    if index == len(word): # Imprtant Base Case #
        return node.end

    if word[index]==".": 
        for ch in node.children: 
            if rep(node.children[ch],word,index+1): 
                return True
        return False  #added later ... if continuing on "." we could not find anything then we should return False so that it return form this brach immediately 
            
    elif word[index] in node.children: 
        return rep(node.children[word[index]],word,index+1)
            
    
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

        


