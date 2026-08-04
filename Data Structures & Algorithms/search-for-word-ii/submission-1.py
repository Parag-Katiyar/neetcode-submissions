def trav(i,j,r,c,state,ans,node,board): 

    if i > r-1 or i < 0 or j > c-1 or j < 0: 
        return 

    if board[i][j] == "#": 
        return

    if board[i][j] not in node.childern: 
        return 

    state.append(board[i][j])
    node = node.childern[board[i][j]]

    if node.end:
        ans.append("".join(state))  # Altering the Trie permanently. 
        node.end = False       #Safe here because each word should be reported only once.

    
    tem = board[i][j]
    board[i][j] = "#"

    if not node.childern: #looking if node.childen is empty means no where to go saves extra computations 
        board[i][j] = tem
        state.pop()
        return

    trav(i+1,j,r,c,state,ans,node,board)
    trav(i-1,j,r,c,state,ans,node,board)
    trav(i,j+1,r,c,state,ans,node,board)
    trav(i,j-1,r,c,state,ans,node,board) 

    board[i][j] = tem
    state.pop()
    return 




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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree = PrefixTree()

        for i in words: 

            tree.insert(i)
        
        r = len(board)
        c = len(board[0])

        state = []
        ans = []
        node = tree.root

        for i in range(0,r): 
            for j in range(0,c):
                state = []
                
                node = tree.root

                trav(i,j,r,c,state,ans,node,board)
        
        return ans

        