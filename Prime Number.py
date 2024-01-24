# For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
 

# Example 1:

# Input:
# N = 5
# Output:
# 1
# Explanation:
# 5 has 2 factors 1 and 5 only.
# Example 2:

# Input:
# N = 25
# Output:
# 0
# Explanation:
# 25 has 3 factors 1, 5, 25

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function isPrime() which takes an integer N as input parameters and returns an integer, 1 if N is a prime number or 0 otherwise.
 

# Expected Time Complexity: O(sqrt(N))
# Expected Space Complexity: O(1)
 

# Constraints:
# 1 <= N <= 109


class Solution:
    def isPrime(self, N):
        """
        Check if a given number N is prime.

        Parameters:
        - N: The number to check for primality.

        Returns:
        - 1 if N is prime, 0 otherwise.
        """
        # Check if N is 0 or 1, which are not prime
        if N == 1 or N == 0:
            return 0  # Not prime
        
        # Iterate through possible divisors from 2 to the square root of N
        for i in range(2, int(N**(1/2)) + 1):
            # If N is divisible by any number in the range, it's not prime
            if N % i == 0:
                return 0  # Not prime

        return 1  # If no divisors are found, N is prime

# Example usage:
solution_obj = Solution()
number_to_check = 17

result = solution_obj.isPrime(number_to_check)
print(number_to_check, "is prime:", bool(result))
