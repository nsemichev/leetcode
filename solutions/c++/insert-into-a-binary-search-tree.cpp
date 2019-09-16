/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode * copyroot = root;
        while(true){
            if(val > copyroot->val){
                if(copyroot->right == NULL){
                    copyroot->right = new TreeNode(val);
                    return root;
                }
                else{
                    copyroot = copyroot->right;
                }
            }
            else{
                if(copyroot->left == NULL){
                    copyroot->left = new TreeNode(val);
                    return root;
                }
                else{
                    copyroot = copyroot->left;
                }
            }
        }
            
    }
};
