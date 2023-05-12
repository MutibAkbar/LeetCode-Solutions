class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashmap_of_3 = dict()
        hashmap_of_rows = dict()
        hashmap_of_cols = dict()
        
        for row in range(0,len(board)):
            for col in range(0,len(board)):
             
                if(board[row][col].isdigit()):
                    hashmap_of_3.setdefault(str(row//3)+str(col//3), []).append(board[row][col])
                    hashmap_of_rows.setdefault(row,[]).append(board[row][col])
                    hashmap_of_cols.setdefault(col,[]).append(board[row][col])
                    
        
        for row in range(0,len(board)):
            if(hashmap_of_cols.get(row)):
                if(len(hashmap_of_cols.get(row)) > len(set(hashmap_of_cols.get(row)))):
                         return False
            if(hashmap_of_rows.get(row)):
                if(len(hashmap_of_rows.get(row)) > len(set(hashmap_of_rows.get(row)))):
                         return False
             
        for row in range(0,len(board)//3):
            for col in range(0,len(board)//3):
                 if(hashmap_of_3.get(str(row)+str(col))):
                    if(len(hashmap_of_3.get(str(row)+str(col))) > len(set(hashmap_of_3.get(str(row)+str(col))))):
                            return False

        return True
      
        