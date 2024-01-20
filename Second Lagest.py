# Given an array Arr of size N, print second largest distinct element from an array.

# Example 1:

# Input: 
# N = 6
# Arr[] = {12, 35, 1, 10, 34, 1}
# Output: 34
# Explanation: The largest element of the 
# array is 35 and the second largest element
# is 34.
# Example 2:

# Input: 
# N = 3
# Arr[] = {10, 5, 10}
# Output: 5
# Explanation: The largest element of 
# the array is 10 and the second 
# largest element is 5.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function print2largest() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. If 2nd largest element doesn't exist then return -1.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 2 ≤ N ≤ 105
# 1 ≤ Arri ≤ 105

class Solution:
    def print2largest(self, arr, n):
        # Find the maximum and minimum values in the array
        fmax = max(arr)
        smax = min(arr)
        
        # Initialize a flag to track if there are distinct elements in the array
        flag = 0
        
        # Iterate through the array to find the second-largest element
        for i in arr:
            if i == fmax:
                # Skip the maximum element
                continue
            flag = 1
            # Update the second-largest element
            smax = max(smax, i)
        
        # If all elements are identical, return -1
        if flag == 0:
            return -1
        
        # Return the second-largest element
        return smax
