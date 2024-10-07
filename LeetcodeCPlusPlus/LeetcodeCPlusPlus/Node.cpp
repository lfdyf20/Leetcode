#include "Node.h"
#include <iostream>

Node::Node(int _val) 
{
	val = _val;
}

Node::Node() 
{
	val = 0;
}

Node::Node(std::vector<int> v)
{
	this->val = 0;

	std::vector<Node*> nodes;
	int currRootIndex = -1;

	for (int i = 0; i < v.size(); i++) 
	{
		int val = v[i];

		if (i == 0)
		{
			this->val = val;
			nodes.push_back(this);
		}
		else if (val == NULL)
		{
			currRootIndex++;
		}
		else 
		{
			nodes.push_back(new Node(val));
			if (currRootIndex != -1 && currRootIndex < nodes.size()) 
			{
				nodes[currRootIndex]->children.push_back(nodes.back());
			}
		}
	}

	if (nodes.size() > 0)
	{
		std::cout << "Tree has been created as follows: \n\n" << std::endl;
		this->print(0, 0, true);
		std::cout << "\n\n" << std::endl;
	}
}

void Node::print()
{
	this->print(0, 0, false);
}

void Node::print(int currDepth, int parentDepth, bool isLastChild) {
	using namespace std;

	if (currDepth == 0)
	{
		cout << this->val << endl;
	}
	else
	{
		for (int i = 0; i < currDepth; i++)
		{
			if (i == parentDepth)
			{
				if (isLastChild)
				{
					cout << "©¸©¤©¤©¤";
				}
				else
				{
					cout << "©À©¤©¤©¤";
				}
			}
			else if (i > parentDepth)
			{
				cout << "    ";
			}
			else
			{
				cout << "©¦   ";
			}
		}
		cout << this->val << endl;
	}

	for (int i = 0; i < this->children.size(); i++)
	{
		this->children[i]->print(currDepth + 1, currDepth, i == this->children.size() - 1);
	}
}