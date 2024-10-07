#pragma once
#include <vector>
#include <string>

class TreeNode
{
public:
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode();
	TreeNode(int x);
	TreeNode(int x, TreeNode* left, TreeNode* right);

	static TreeNode* createTree(std::vector<int> v);
};
