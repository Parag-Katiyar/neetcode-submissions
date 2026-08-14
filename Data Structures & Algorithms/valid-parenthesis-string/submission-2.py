class Solution:
    def checkValidString(self, s: str) -> bool:
        # Instead of integer counts, we store the indices (positions)
        # of the open brackets and asterisks
        num_1 = []  # Stores indices of '('
        num_s = []  # Stores indices of '*'
        
        # Enumerate gives us both the index (idx) and the character (i)
        for idx, i in enumerate(s): 
            if i == "(": 
                num_1.append(idx)
            if i == "*": 
                num_s.append(idx)
            if i == ")": 
                # First, try to balance with an open bracket '('
                if num_1:
                    num_1.pop()
                # If no '(', try to balance with an asterisk '*'
                elif num_s:
                    num_s.pop()
                # If neither is available, the order is invalid
                else:
                    return False

        # After the loop, match remaining '(' with remaining '*'
        # The '*' MUST appear after the '(' to close it (idx_s > idx_1)
        while num_1 and num_s:
            if num_1[-1] > num_s[-1]:
                return False  # '(' is after '*', so '*' cannot close it
            num_1.pop()
            num_s.pop()
            
        # If all open brackets are successfully matched, the string is valid
        if len(num_1) == 0: 
            return True

        return False