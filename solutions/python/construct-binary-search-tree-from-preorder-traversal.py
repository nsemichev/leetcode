class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if(len(preorder) == 0):
            return None
        #if(len(preorder) == 1):
        #    return TreeNode(preorder[0])
        first = preorder[0]
        root = TreeNode(first)
        ind = 0
        for i in range(1, len(preorder)):
            if first < preorder[i]:
                ind = i
                break
        if ind == 0:
            ind = len(preorder)
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right = self.bstFromPreorder(preorder[ind:])
        return root
