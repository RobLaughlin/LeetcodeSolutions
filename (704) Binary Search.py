# (704) Binary Search
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# https://leetcode.com/problems/binary-search/

def search(nums, target):
    if len(nums) == 0:
        return -1
    
    l = 0
    r = len(nums)-1
    i = 0
    while (r >= l):
        i = (r + l) // 2

        if nums[i] > target:
            r = i-1
        elif nums[i] < target:
            l = i+1
        else:
            return i
    
    return -1

if __name__ == '__main__':
    nums = [1,2,3,5,7,9]
    target = 2.5

    print(search(nums, target))