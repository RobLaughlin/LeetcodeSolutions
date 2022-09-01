from cmath import inf
from queue import Queue

"""
(1448) Count Good Nodes in Binary Tree
Given a binary tree root, 
a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        q = Queue()
        q.put(self)
        tree = []

        while not q.empty():
            node = q.get()
            
            if node != None:
                q.put(node.left)
                q.put(node.right)
                tree.append(node.val)
            else:
                tree.append(None)
        
        return str(tree)
    
def DFSCount(node: TreeNode, maxVal=-inf):
    if node is None or node.val is None:
        return 0
    
    if node.val >= maxVal:
        return 1 + DFSCount(node.left, node.val) + DFSCount(node.right, node.val)
    
    return DFSCount(node.left, maxVal) + DFSCount(node.right, maxVal)

def parseTree(tree):
    if len(tree) == 0:
        return TreeNode(None)
    
    tree = list(map(lambda val: TreeNode(val), tree))
    root = tree[0]

    for i in range(1, len(tree)):
        parent = tree[(i-1) // 2]
        node = tree[i]

        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node


    return root

if __name__ == '__main__':
    tree = [3,3,None,4,2]
    root = parseTree(tree)
    print(DFSCount(root))

        
