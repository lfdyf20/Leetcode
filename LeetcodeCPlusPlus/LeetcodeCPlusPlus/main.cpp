#include <iostream>
#include "Printer.h"
#include "Node.h"
#include "Maximum Depth of N-ary Tree.h"

int main() {
	Printer printer;
	
	// test case: [1,null,3,2,4,null,5,6]
	std::vector<int> v = { 1, NULL, 3, 2, 4, NULL, 5, 6 };
	Node* root = new Node(v);
	Solution s;
	printer.print(s.maxDepth(root));
}