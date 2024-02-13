class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for brace in s:
            
            # If it's an opening brace, simply push it in our stack
            if brace not in close_to_open:
                stack.append(brace)
            
            # This means we have encountered a closing brace 
            else:
                
                # Before doing anything, first let's grab the top element from our 
                stack_top_element = stack.pop() if stack else "F"

                # Now check if stack_top_element is a valid open brace 
                if close_to_open[brace] != stack_top_element:
                    return False 
        
        # It may happen you have some opening braces that weren't ever closed 

        return not stack