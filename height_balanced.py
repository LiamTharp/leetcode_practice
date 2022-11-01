from typing import Optional 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        max = self.dfs(root, function = max, height = 0)

        min = self.dfs(root.right, function = min, height = 0)

    
    def dfs(self, function, root, height = 0) -> int:
        
        if root:
            left = self.dfs(root.left)
            right = self.dfs(root.right)

            height += function(left, right) + 1
        
        return height