#pragma once
#include "Node.h"

class Solution {
public:
    int maxDepth(Node* root) {
		if (root == NULL) 
		{
			return 0;
		}

		if (root->children.size() == 0) 
		{
			return 1;
		}

		int maxDepth = 0;
		for (Node* child : root->children)
		{
			int childDepth = this->maxDepth(child);
			if (childDepth > maxDepth)
			{
				maxDepth = childDepth;
			}
		}

		return maxDepth + 1;
    }
};