# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        l = len(nums)
        if l == 0:
            return None;
        mx = max(nums)
        ind = nums.index(mx)
        
        newNode = TreeNode(mx)
        newNode.left = self.constructMaximumBinaryTree(nums[0:ind])
        newNode.right = self.constructMaximumBinaryTree(nums[ind+1:l])
        return newNode
            
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
