"""
(637) Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""

from logging import root
from queue import Queue

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

def parseTree(tree):
    if len(tree) == 0:
        return TreeNode(None)
    
    tree = list(map(lambda val: TreeNode(val), tree))
    root = tree[0]

    for i in range(1, len(tree)):
        parent = tree[(i-1) // 2]
        node = tree[i]
        if node.val is None:
            continue

        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node


    return root

def averageOfLevels(root):
    q = Queue()
    q.put(root)
    averages = []
    
    while not q.empty():
        total = 0
        qsize = q.qsize()
        
        for _ in range(qsize):
            node = q.get()
            total += node.val
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            
        averages.append(total / qsize)
    
    return averages

if __name__ == '__main__':
    tree = [3,9,20,None,None,15,7]
    root = parseTree(tree)
    print(root)
    print(averageOfLevels(root))
