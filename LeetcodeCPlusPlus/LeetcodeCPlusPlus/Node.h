#pragma once
#include <vector>


class Node {
public:
    int val;
    std::vector<Node*> children;

    Node();

    Node(int _val);

    Node(std::vector<int> v);

    void print(int currDepth, int parentDepth, bool isLastChild);
};
