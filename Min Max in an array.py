# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

 

# Example 1:

# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.
 

# Example 2:

# Input:
# N = 5
# A[]  = {1, 345, 234, 21, 56789}
# Output: 1 56789
# Explanation: minimum and maximum element of array are 1 and 56789.
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function getMinMax() which takes the array A[] and its size N as inputs and returns the minimum and maximum element of the array.

 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

 

# Constraints:
# 1 <= N <= 105
# 1 <= Ai <=1012


def getMinMax(a, n):
    """
    Find the minimum and maximum elements in the given array.

    Parameters:
    - a: The array to find minimum and maximum elements from.
    - n: Size of the array.

    Returns:
    - List containing [minimum, maximum].
    """
    # Initialize minimum and maximum to extreme values
    mini = float('inf')  # set to positive infinity
    maxi = float('-inf')  # set to negative infinity
    
    # Iterate through the array elements
    for i in a:
        # Update minimum if current element is smaller
        if i < mini:
            mini = i
        # Update maximum if current element is larger
        if i > maxi:
            maxi = i

    return [mini, maxi]  # Return the list containing minimum and maximum

# Example usage:
array_to_process = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
size_of_array = len(array_to_process)

result = getMinMax(array_to_process, size_of_array)
print("Minimum and Maximum elements:", result)
