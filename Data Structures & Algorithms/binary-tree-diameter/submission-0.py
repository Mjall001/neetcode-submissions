# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #longest path(allleft+allright) vs onenodes(allright+allleft)
        #use res to save and max the value each run

        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter
            if not root: return 0

            left,right = dfs(root.left),dfs(root.right)
            maxDiameter = max(maxDiameter,left+right)

            return 1 + max(left,right)


        dfs(root)
        return maxDiameter
