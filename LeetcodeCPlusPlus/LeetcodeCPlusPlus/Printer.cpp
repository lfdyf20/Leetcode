#include "Printer.h"


void Printer::print(int n) {
	std::cout << n << std::endl;
}

void Printer::print(bool b)
{
	std::cout << (b ? "true" : "false") << std::endl;
}

void Printer::print(std::vector<int> v) {
	std::cout << "[";
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i];
		if (i != v.size() - 1) {
			std::cout << ", ";
		}
	}
	std::cout << "]" << std::endl;
}

void Printer::print(std::vector<std::vector<int>> v) {
	std::cout << "[" << std::endl;
	for (int i = 0; i < v.size(); i++) {
		std::cout << "  ";
		print(v[i]);
	}
	std::cout << "]" << std::endl;
}