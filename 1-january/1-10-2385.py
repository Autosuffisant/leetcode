# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Use breadth first search from start to find the longest path
        # to a leaf node
        queue = [(root, 0)]
        max_depth = 0

        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left, depth + node.left.val))

            if node.right:
                queue.append((node.right, depth + node.right.val))

        return max_depth
