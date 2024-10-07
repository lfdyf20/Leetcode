#include "TreeNode.h"
#include <iostream>
#include <queue>
#include <cmath>
#include <iomanip>


TreeNode::TreeNode() : val(0), left(nullptr), right(nullptr) {}
TreeNode::TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
TreeNode::TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}

TreeNode* TreeNode::createTree(std::vector<int> v)
{
	if (v.size() == 0)
	{
		return nullptr;
	}

	TreeNode* root = new TreeNode(v[0]);
	std::vector<TreeNode*> nodes;
	nodes.push_back(root);

	for (int i = 1; i < v.size(); i++)
	{
		if (v[i] == NULL)
		{
			continue;
		}

		TreeNode* node = new TreeNode(v[i]);
		nodes.push_back(node);

		int parentIndex = (i - 1) / 2;
		if (i % 2 == 0)
		{
			nodes[parentIndex]->right = node;
		}
		else
		{
			nodes[parentIndex]->left = node;
		}
	}

	return root;
}