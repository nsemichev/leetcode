# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        
        if len(S) == 0:
            return None
        splt = S.split("-")
        root = TreeNode(splt[0])
        if len(splt) == 1:
            return root
        if len(splt) == 2:
            root.left = TreeNode(splt[1])
            return root
        left = ""
        right = ""
        leftStart = False
        rightStart = False
        dashCount = 0
        for symb in S:
            if symb == '-':
                dashCount += 1
            else:
                if dashCount == 1:
                    if leftStart:
                        rightStart = True
                        leftStart = False
                    else:
                        leftStart = True
                else:
                    if leftStart:
                        left += '-' * (dashCount - 1)
                    else:
                        right += '-' * (dashCount - 1)
                        
                if leftStart:
                    left += symb
                elif rightStart:
                    right += symb
                    
                dashCount = 0

        leftTree = self.recoverFromPreorder(left)
        rightTree = self.recoverFromPreorder(right)
        root.left = leftTree
        root.right = rightTree
        
        return root
        
