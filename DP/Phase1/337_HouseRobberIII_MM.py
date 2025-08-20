from functools import lru_cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def make_recursion(IE, node):

            if not node:
                return 0
            
            # Include
            if IE==1:
                include = node.val + make_recursion(0, node.left) + make_recursion(0, node.right)
                exclude = make_recursion(1, node.left) + make_recursion(1, node.right)
                return include if include > exclude else exclude

            # Exclude
            if IE==0:
                return make_recursion(1, node.left) + make_recursion(1, node.right)
                
        def make_recursionx(x):
            if x:
                make_recursionx(x.left)
                print(x.val)
                make_recursionx(x.right)
            else:
                print(f"x is {x}")


        return make_recursion(1, root)