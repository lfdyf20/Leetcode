#pragma once

#include "TreeNode.h"
#include <deque>


class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
		std::vector<int> v;

		inorder(root, v);

		for (int i = 0; i < v.size(); i++)
		{
			for (int j = i + 1; j < v.size(); j++)
			{
				if (v[i] + v[j] == k)
				{
					return true;
				}
			}
		}

		return false;
    }

	void inorder(TreeNode* root, std::vector<int>& v)
	{
		TreeNode* curr = root;
		std::deque<TreeNode*> stack;

		while (curr != NULL || !stack.empty())
		{
			while (curr != NULL)
			{
				stack.push_back(curr);
				curr = curr->left;
			}

			curr = stack.back();
			stack.pop_back();

			v.push_back(curr->val);

			curr = curr->right;
		}
	}
};