"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
"""
Brute force solution to the problem -> O(n^2)
We loop through the entire array, for every element we loop through all the elements again 
and skip the one at the same index
return the new array with the product at each index
"""
def brute_force(A):
    total = A.copy()
    for i in range(len(A)):
        sum=1
        for j in range(len(A)):
            if i==j:
                continue
            else:
                sum *= A[j]
        total[i] = sum
    return total
"""
Optimized solution -> O(2n)=O(n)
We first loop through the entire array to obtain the product of all the items
Then we loop through it again and divide the sum by each element at the corresponding index
we return the new index
"""
def optimized(A):
    total = A.copy()
    mult=1
    for num in A:
        mult *=num
    
    for i in range(len(A)):
        total[i] = mult // A[i]
    return total

"""
Solution without using division -> O(nxm)
In this solution, we multiply what is left of i everytime we go through i, and j multiplies the right part.
After each i, j has less length(m) to go through. making this algorithm better than the brute force 
"""
def no_division(A):
    total = A.copy()
    left = 1
    for i in range(len(A)):
        right =1
        if i>0: 
            left *= A[i-1]
        for j in range(i+1,len(A)):
            right *= A[j]
        total[i] = left * right
    return total

print(no_division([1, 2, 3, 4, 5]))