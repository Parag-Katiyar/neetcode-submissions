def find(r,c,x,y,index, wd_len,board, word): 

    if index == wd_len: 
        return True

    if x+1 <= r-1 and y >= 0 and y <= c-1 and x+1 >= 0 and board[x+1][y] == word[index]: 
        tem = board[x+1][y]
        board[x+1][y] = "#"

        if find(r,c,x+1,y,index+1,wd_len,board, word): 
            board[x+1][y] = tem
            return True  
        board[x+1][y] = tem

    if x-1 >= 0 and x-1 <= r-1 and y >= 0 and y <= c-1 and board[x-1][y] == word[index]:
        tem = board[x-1][y]
        board[x-1][y] = "#"

        if find(r,c,x-1,y,index+1,wd_len,board, word): 
            board[x-1][y] = tem
            return True
        board[x-1][y] = tem  
        

    if x <= r-1 and y+1 >= 0 and y+1 <= c-1 and x >= 0 and board[x][y+1] == word[index] :
        tem = board[x][y+1]
        board[x][y+1] = "#"
        if find(r,c,x,y+1,index+1,wd_len,board, word):
            board[x][y+1] = tem 
            return True 
        board[x][y+1] = tem

    if x <= r-1 and y-1 >= 0 and y-1 <= c-1 and x >= 0 and board[x][y-1] == word[index]:
        tem = board[x][y-1]
        board[x][y-1] = "#"
        if find(r,c,x,y-1,index+1,wd_len,board, word): 
            board[x][y-1] = tem
            return True 
        board[x][y-1] = tem

    return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        r = len(board)
        c = len(board[0])
        wd = list(word)
        wd_len = len(word)


        for i in range(0,r): 
            for j in range(0,c): 

                if board[i][j] == wd[0]:
                    tex = board[i][j]
                    board[i][j] = "#"
                    x = i 
                    y = j 
                    if find(r,c,x,y,1,wd_len,board, word): 
                        board[i][j] = tex
                        return True
                    board[i][j] = tex 
        return False 

            










        