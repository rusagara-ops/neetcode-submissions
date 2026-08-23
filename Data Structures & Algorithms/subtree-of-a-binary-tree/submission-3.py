# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        if self.issametree(root, subRoot):
            return True
            
        return self.issametree(root.left, subRoot) or self.issametree(root.right, subRoot)
        
    
    def issametree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.issametree(p.left, q.left) and self.issametree(p.right, q.right))