class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, elem):
        self.stack.append(elem)
    
    def pop(self):
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)

class MaxStack(Stack):
    def max(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1][1]
    
    def push(self, elem):
        maxElem = self.max()

        if maxElem is None or elem >= maxElem:
            super().push((elem, elem))
        else:
            super().push((elem, maxElem))
    
    def pop(self):
        elem, _ = super().pop()
        return elem

class MaxQueue:
    def __init__(self):
        self.eq = MaxStack()
        self.dq = MaxStack()
    
    def enqueue(self, elem):
        self.eq.push(elem)
    
    def dequeue(self):
        if len(self.dq) == 0:
            while len(self.eq) > 0:
                self.dq.push(self.eq.pop())
        
        if len(self.dq) == 0:
            raise Exception("Nothing in the queue to dequeue.")
        
        return self.dq.pop()
    
    def max(self):
        Leq = len(self.eq)
        Ldq = len(self.dq)

        if Leq == 0 and Ldq == 0:
            return None
        elif Leq != 0 and Ldq == 0:
            return self.eq.max()
        elif Leq == 0 and Ldq != 0:
            return self.dq.max()
        else:
            return max(self.eq.max(), self.dq.max())
    
    def __len__(self):
        return len(self.eq) + len(self.dq)

"""
(239) Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
class Solution:
    def maxSlidingWindow(self, nums, k):
        mq = MaxQueue()
        for i in range(k):
            mq.enqueue(nums[i])
        
        maxWindow = [mq.max()]
        for i in range(k, len(nums)):
            mq.enqueue(nums[i])
            mq.dequeue()
            maxWindow.append(mq.max())
        
        return maxWindow

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    print("INPUT:", nums)
    print("OUTPUT:", sol.maxSlidingWindow(nums, k))