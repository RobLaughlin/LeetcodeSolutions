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
        # Sort the candidates first, then when we know a candidate sum doesn't work,
        # any candidate with a sum greater than target will also not work.
        # We can use this method to trim the tree of combinations.
        
        combinations = []
        if len(candidates) == 0:
            return []
        
        candidates = sorted(candidates)
        maxMultipliers = list(map(lambda c: target // c, candidates))
        stack = [maxMultipliers[0]]
        
        total = maxMultipliers[0]*candidates[0]
        while len(stack) > 0:            
            i = len(stack)-1
            candidate = candidates[i]

            if stack[-1] < 0:
                total += candidate*(-stack[-1])
                stack.pop()
                continue

            if total > target:
                stack[-1] -= 1
                total -= candidate
            elif total == target:
                combination = []
                for j in range(len(stack)):
                    m = stack[j]
                    combination.extend([candidates[j]]*m)
                
                combinations.append(combination)
                stack[-1] -= 1
                total -= candidate
            elif len(stack) == len(candidates):
                while len(stack) > 0 and stack[-1] == 0:
                    stack.pop()
                
                if len(stack) > 0:
                    stack[-1] -= 1
                    i = len(stack)-1
                    candidate = candidates[i]
                    total -= candidate
            else:
                # pick the biggest multiplier that works
                nextCandidate = candidates[i+1]
                multiplier = (target - total) // nextCandidate

                if multiplier == 0:
                    while len(stack) > 0 and stack[-1] == 0:
                        stack.pop()
                    
                    if len(stack) > 0:
                        stack[-1] -= 1
                        i = len(stack)-1
                        candidate = candidates[i]
                        total -= candidate
                else:
                    stack.append(multiplier)
                    total += nextCandidate*multiplier
                
        return combinations
                    
if __name__ == '__main__':
    sol = Solution()
    target = 7
    candidates = [6,7,2,3]
    combinations = sol.combinationSum(candidates, target)
    print(combinations)