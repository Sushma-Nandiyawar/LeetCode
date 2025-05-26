class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        while i<n:
            while i<n and path[i] == '/':
                i += 1
            start = i
            while i<n and path[i] != '/':
                i += 1
            part = path[start:i]

            if part =='.' or part =='':
                continue
            if part =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/'+'/'.join(stack)

            
