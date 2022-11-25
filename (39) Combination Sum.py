"""
(39) Combination Sum
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to 
target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates, target):
        # Use depth-first search with 'path' memoization to not explore paths you've already explored.
        # a 'path' in this case is a candidate representation of a target.
        visited = set()
        combinations = []

        stack = [(target, tuple([0]*len(candidates)))]
        while len(stack) > 0:
            nextTarget, frequency = stack.pop()
            if frequency in visited:
                continue

            visited.add(frequency)
            if nextTarget == 0:
                combination = []
                for i in range(len(candidates)):
                    f = frequency[i]
                    candidate = candidates[i]
                    combination.extend([candidate]*f)
                
                combinations.append(combination)
                continue

            for i in range(len(candidates)):
                candidate = candidates[i]
                child = nextTarget - candidate
                if child >= 0:
                    childFreq = list(frequency)
                    childFreq[i] += 1
                    stack.append((child, tuple(childFreq)))
        
        return combinations
            
if __name__ == '__main__':
    sol = Solution()
    target = 8
    candidates = [2,3,5]
    print(sol.combinationSum(candidates, target))
