"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

"""
***These assumptions are to be considered, 1 is the smallest positive integer
We go through the list and if we find a number that is not at it's place (i+1) we switch it with where it should be
contingent that the number is not bigger than the length(since we start at 1, we can go all through len of list)
if the number is where it's supposed to be , we go to the other one,if the number is duplicate, we skip too 
if the number is negative or more than length, we ignore it. We only worry about the smallest missing positive, 
things will fall in places afterwards.
"""
def smallest_missing(nums):
    for i,num in enumerate(nums):
        while nums[i] != i+1 and 0 < nums[i]< len(nums):
            new_ind = nums[i]-1
            nums[i],nums[new_ind] = nums[new_ind],nums[i]
            if nums[i] == nums[new_ind]:
                break
    "We go throuh the list with each item where it's supposed to belong, if it doesn't then it's missing, we return it"
    for i, num in enumerate(nums,1):
        if num !=i:
            return i
    "if we went through the whole list and all was found at it's place, we return the next item"        
    return len(nums)+1




print(smallest_missing([1, 2, 0] ))