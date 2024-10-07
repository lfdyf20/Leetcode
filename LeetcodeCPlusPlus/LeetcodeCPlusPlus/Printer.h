#pragma once

#include <iostream>
#include <vector>

class Printer {
public:
	void print(int n);
	void print(bool b);
	void print(std::vector<int> v);
	void print(std::vector<std::vector<int>> v);
};