from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        MOD = 10**9 + 7
        tree_sum, max_product = 0, 0
        def dfs(root):
            if not root:
                return 0
            root.val += dfs(root.left) + dfs(root.right)
            return root.val

        tree_sum = dfs(root)
        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            product = (tree_sum - cur_node.val) * cur_node.val
            max_product = max(max_product, product)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return max_product % MOD
