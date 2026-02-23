class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        stack = []
        path_c = path.split("/")

        for char in path_c:
            if char == ".." and stack:
                stack.pop()
            elif char == "" or char == "." or char == "..":
                continue
            else:
                stack.append(char)
      
        return "/" + "/".join(stack)
