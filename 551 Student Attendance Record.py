# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

 

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.

class Solution:
    def checkRecord(self, s: str) -> bool:
        # Initialize a variable to count the occurrences of 'A'
        n = 0

        # Iterate through the characters in the string
        for i in range(len(s)):
            # Check if the current character is 'A'
            if s[i] == 'A':
                n += 1

            # If more than one 'A' is found, return False
            if n > 1:
                return False

            # Check for consecutive 'L's
            if i < len(s) - 2:
                if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                    return False

        # If no issues found, return True
        return True
