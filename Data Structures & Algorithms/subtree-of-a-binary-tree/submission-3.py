# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #two recursive jobs
        #isSubtree matches roots
        #dfsMatch matches nodes on every leverl
        #isSubtree returns False on: root not subRoot
        #and True on not Subroot
        #call self.isSubtree on right and left nodes
        # if root.val == subRoot.val:
        #  dfsMatch(root.left,subroot.light)
        if not root:return False

        if not subRoot: return True
        
        if (self.dfsMatch(root,subRoot)):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def dfsMatch(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False
        
        return self.dfsMatch(root.left,subRoot.left) and self.dfsMatch(root.right,subRoot.right)
        
        
        
        




