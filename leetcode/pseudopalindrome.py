# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        def dfs(node, path_count):
            if not node:
                return 0
            
            path_count[node.val] += 1
            
            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                odd_count = sum(count % 2 for count in path_count.values())
                return 1 if odd_count <= 1 else 0
            
            # Recursive calls for left and right children
            left_count = dfs(node.left, path_count.copy())
            right_count = dfs(node.right, path_count.copy())
            
            return left_count + right_count
        
        # Initialize a dictionary to keep track of digit counts in the path
        initial_path_count = {digit: 0 for digit in range(1, 10)}
        
        # Start DFS from the root
        return dfs(root, initial_path_count)
