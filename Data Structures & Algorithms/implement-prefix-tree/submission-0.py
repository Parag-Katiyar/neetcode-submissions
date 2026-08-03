class tnode: 
    def __init__(self): 
        self.childern = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = tnode()

    def insert(self, word: str) -> None:

        node = self.root

        for w in word:
            if w not in node.childern: 
                node.childern[w] = tnode()
            node = node.childern[w]

        node.end = True


    def search(self, word: str) -> bool:

        node = self.root

        for w in word: 
            if w not in node.childern: 
                return False 
            node = node.childern[w]
        return node.end  
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root 

        for w in prefix: 

            if w not in node.childern: 
                return False 

            node = node.childern[w]

        return True







        
        