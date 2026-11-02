# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both trees null return true
        #if only 1 is null return false
        #is.val isn't equal return false
        #if .val is equal recusivly call the function on left,right
        # return (left and right) which should evaluate to true

        if not p and not q: return True
        if (not p or not q) or (p.val != q.val): return False

        return ((self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right)))
        