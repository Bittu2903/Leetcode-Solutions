# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 

# Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric.

        Parameters:
        - root: Root node of the binary tree.

        Returns:
        - True if the binary tree is symmetric, False otherwise.
        """
        def isMirror(p, q):
            """
            Helper function to check if two subtrees are mirrors of each other.

            Parameters:
            - p: Root node of the first subtree.
            - q: Root node of the second subtree.

            Returns:
            - True if the subtrees are mirrors, False otherwise.
            """
            # If both nodes are None, the subtrees are mirrors
            if not p and not q:
                return True

            # If one of the nodes is not None and their values are equal,
            # check if the left subtree of the first is the mirror of the right subtree of the second
            # and vice versa
            if p is not None and q is not None and p.val == q.val:
                return isMirror(p.left, q.right) and isMirror(p.right, q.left)

            return False

        # Call the helper function with the root of the binary tree as both subtrees
        return isMirror(root, root)
