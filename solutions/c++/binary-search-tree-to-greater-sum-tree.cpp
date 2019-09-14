/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <vector>
#include <iterator>
#include <iostream>
using namespace std;

vector<TreeNode *> nodes;

void in_order_traversal(TreeNode* root){
    if(root == NULL) return;
    if(root -> left != NULL){
        in_order_traversal(root->left);
    }
    nodes.push_back(root);
    if(root -> right != NULL){
        in_order_traversal(root->right);
    }
}
class Solution {
public:
    
    
    TreeNode* bstToGst(TreeNode* root) {
        in_order_traversal(root);
        int sum = 0;
        for(int i = nodes.size()-1; i >= 0; i--){
            sum += nodes[i]->val;
            nodes[i]->val = sum;
        }
        nodes.clear();
        return root;
    }
};
