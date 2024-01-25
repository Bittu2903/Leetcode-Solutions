# You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

# Return the maximum strength of a group the teacher can create.

 

# Example 1:

# Input: nums = [3,-1,-5,2,5,-9]
# Output: 1350
# Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
# Example 2:

# Input: nums = [-4,-5,-4]
# Output: 20
# Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 

# Constraints:

# 1 <= nums.length <= 13
# -9 <= nums[i] <= 9


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Separate positive and negative numbers
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num <= 0]

        # If there are no positives and only one negative, return that negative value
        if not positives and len(negatives) == 1:
            return negatives[0]

        # Sort positives in descending order and negatives in ascending order
        positives.sort(reverse=True)
        negatives.sort()

        result = 1

        # Calculate the product of positive numbers
        for num in positives:
            result *= num

        # If there are no negatives, the result is the product of all positive numbers
        if not negatives:
            return result

        maximum = 0

        # Calculate the product of negative numbers and update maximum
        for num in negatives:
            # Update maximum if it is 0 and there are positive numbers
            if maximum == 0 and positives:
                maximum = result

            result *= num
            # Update maximum if the current result is greater
            maximum = max(maximum, result)

        return maximum
