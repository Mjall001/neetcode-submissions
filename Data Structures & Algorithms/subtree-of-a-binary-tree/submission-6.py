# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # use isSubtree to travese until match is found
        # use dfsmatch to make sure both roots match
        # iterate until end of root or dfsMatch = true
        # end condition for isSubtree should be root None

        if not root: return False

        if not subRoot: return True

        #create another end condition subroot==root
        #that returns true and ends recursion
        if root.val == subRoot.val and self.dfsMatch(root,subRoot):
            return True #only be returned if true otherwise keep going until end of root
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        #dfsMatch matching root here


    def dfsMatch(self, root, subRoot):
        if not subRoot and not root: return True
        if not root or not subRoot: return False
        if ((root.val == subRoot.val) and
        (self.dfsMatch(root.left,subRoot.left) and
        self.dfsMatch(root.right,subRoot.right))):
            return True

        return False
    