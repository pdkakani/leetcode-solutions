class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_c = path.split("/")

        for c in path_c:
            if c == ".." and stack:
                stack.pop()
            elif c == "" or c == "." or c == "..":
                continue
            else:
                stack.append(c)
            
        return "/" + "/".join(stack)
        
