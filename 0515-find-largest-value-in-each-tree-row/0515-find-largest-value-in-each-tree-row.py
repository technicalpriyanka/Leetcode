# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        queue=[root]
        while queue:
            ans.append(max(node.val for node in queue))
            next_level_queue=[]
            for node in queue:
                for child in (node.left, node.right):
                    if child:
                        next_level_queue.append(child)
                queue = next_level_queue
        return ans
        
        
        
        