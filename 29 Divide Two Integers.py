# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Save the original divisor for reference
        orig_divisor = divisor
        # Initialize the quotient
        n = 0

        # Handle the case where either dividend or divisor is zero
        if dividend == 0:
            return 0

        # Determine the sign of the result
        sign = (dividend > 0) == (divisor > 0)

        # Handle the case where divisor is 1 or -1 separately
        if divisor == 1:
            return dividend
        elif divisor == -1:
            # Handle division by -1, considering overflow cases
            dividend = dividend if sign else -dividend
            return min(max(dividend, -2**31), 2**31 - 1)

        # Take the absolute values for calculation
        dividend, divisor = abs(dividend), abs(divisor)

        # Main division logic
        while dividend >= divisor:
            dividend -= divisor
            n += 1

        # Apply the sign to the result
        result = n if sign else -n

        # Limit the result within the 32-bit signed integer range
        return min(max(result, -2**31), 2**31 - 1)
