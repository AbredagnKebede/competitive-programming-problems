class Solution:
    def simplifyPath(self, path: str) -> str:
        
        components = path.split('/')
        my_stack = []
        for component in components:
            print(component)
            if component == '..':
                if my_stack:
                    my_stack.pop()
            elif component and component!='.':
                my_stack.append(component)
        
        results = '/'+ '/'.join(my_stack)

        return results

