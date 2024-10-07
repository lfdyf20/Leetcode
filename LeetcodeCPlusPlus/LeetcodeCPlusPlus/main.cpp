#include <iostream>
#include "Printer.h"
#include "Node.h"
#include "TreeNode.h"


#include "Two Sum IV - Input is a BST.h"

int main() {
	Printer printer;
	Solution solution;
	
	// test case: [5,3,6,2,4,null,7]
	std::vector<int> v = { 5,3,6,2,4,NULL,7 };
	TreeNode* root = TreeNode::createTree(v);
	
	printer.print(solution.findTarget(root, 9)); // expected: true
}