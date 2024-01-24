# Given an array A[] of size n. The task is to find the largest element in it.
 

# Example 1:

# Input:
# n = 5
# A[] = {1, 8, 7, 56, 90}
# Output:
# 90
# Explanation:
# The largest element of given array is 90.
 

# Example 2:

# Input:
# n = 7
# A[] = {1, 2, 0, 3, 2, 4, 5}
# Output:
# 5
# Explanation:
# The largest element of given array is 5.
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function largest() which takes the array A[] and its size n as inputs and returns the maximum element in the array.

 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

 

# Constraints:
# 1 <= n<= 103
# 0 <= A[i] <= 103
# Array may contain duplicate elements. 

def largest(arr, n):
    """
    Find the largest element in the given array.

    Parameters:
    - arr: The array to find the largest element from.
    - n: Size of the array.

    Returns:
    - The largest element in the array.
    """
    # Initialize the maximum value to negative infinity
    maxi = float('-inf')
    
    # Iterate through the array elements
    for i in arr:
        # Update maximum if the current element is larger
        if i > maxi:
            maxi = i

    return maxi  # Return the largest element

# Example usage:
array_to_process = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
size_of_array = len(array_to_process)

result = largest(array_to_process, size_of_array)
print("Largest element:", result)