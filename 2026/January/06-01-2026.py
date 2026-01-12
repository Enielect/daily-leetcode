from collections import deque
from typing import Optional

## I think that for bfs you keep track of the nodes that you are yet to visit in 
## a deque and pop from the front for all unvisited nodes


# I had issues with a testcase so Elias told me to opt for a better way to do it.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(head: TreeNode):
    root = deque([(1, head)])
    max_sum, prv_lvl = (1, 0), 1
    cur_sum = 0

    while root:
        level, cur = root.popleft()
        if level == prv_lvl:
            cur_sum += cur.val
        else:
            max_sum = (prv_lvl, cur_sum) if cur_sum > max_sum[1] else max_sum
            prv_lvl, cur_sum = level, cur.val
        
        if cur.left:
            root.append((level + 1, cur.left))
        if cur.right:
            root.append((level + 1, cur.right))
    return max_sum[0]


## second and better approach

# class Solution:
#     def maxLevelSum(self, root: TreeNode) -> int:
#             nodes = deque([root])
#             max_sum, lvl= (1, float('-inf')), 1

#             while nodes:
#                 qlen, cur_sum = len(nodes), 0
#                 for _ in range(qlen):
#                     cur = nodes.popleft()
#                     cur_sum += cur.val
#                     if cur.left:
#                         nodes.append(cur.left)
#                     if cur.right:
#                         nodes.append(cur.right)
#                 max_sum = (lvl, cur_sum) if cur_sum > max_sum[1] else max_sum
#                 lvl +=1
#             return max_sum[0]



root = TreeNode(1)
root.left = TreeNode(7)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right = TreeNode(0)

print(bfs(root))