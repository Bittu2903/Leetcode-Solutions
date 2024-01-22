# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104
 

# Follow up: Could you write a solution that works in logarithmic time complexity?

# We are checking prime factors in 2 and 5 so to get zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n < 0):
            return -1

        count = 0

        while(n >= 5):
            n //= 5
            count += n

        return count