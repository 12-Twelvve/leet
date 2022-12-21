# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# my_solution - 145ms
class Solution():
    def largestValues(self, root):
        queue1 = []
        queue2 = []
        result = []
        if root == None:
            return []
        result.append(root.val)
        if root.left:
            queue1.append(root.left)
        if root.right:
            queue1.append(root.right)

        def checkQueue(que, emptyqueue):
            rowMax = que[0].val
            for node in que:
                if rowMax < node.val:
                    rowMax = node.val
                if node.left:
                    emptyqueue.append(node.left)
                if node.right:
                    emptyqueue.append(node.right)
            return rowMax, emptyqueue

        while True:
            if len(queue1) > 0:
                val, queue2 = checkQueue(queue1, queue2)
                result.append(val)
                queue1 = []
            elif len(queue2) > 0:
                val, queue1 = checkQueue(queue2, queue1)
                result.append(val)
                queue2 = []
            else:
                break
            print(result)
        return result

# --- simple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def largestValues(self, root):
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(max(level))

        return res

# best
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)

        result = []

        while queue:

            result.append(max([node.val for node in queue]))

            new_queue = collections.deque()

            for node in queue:
                for child in [node.left, node.right]:
                    if child:
                        new_queue.append(child)

            queue = new_queue

        return result
        # T: O(N)
        # S: O(N)