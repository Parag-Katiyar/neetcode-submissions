def rep(node,word,index): 

    if index == len(word): 
        return node.end


    for x in range(index,len(word)):

        if word[x] ==".":

            for ch in node.children:

                if rep(node.children[ch],word,x+1): 
                    return True
            return False 

        if word[x] not in node.children: 
            return False  

        node = node.children[word[x]]

    return node.end  
     
     

   
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


        
        



        