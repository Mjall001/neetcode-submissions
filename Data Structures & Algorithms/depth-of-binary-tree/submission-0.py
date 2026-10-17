# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursion call on self return 1+ itself

        #breadth depth search
        #while root(doublequeue thatcontains treenode)
         #for root length:
          #node = popleft(root)
          #if node.left != None
           #root.append(node.left)
          #if node.right != None
           #root.append(node.right)
        #level = level+1

        if root == None:
            return 0
        que = deque()
        que.append(root)

        level = 0

        while que:
            for i in range(len((que))):
                node = que.popleft()
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
            level = level+1

        return level





