#include <vector>;
#include <iostream>
#include "Printer.h"

using namespace std;

class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
		int maxLength = 1;
		int currIncrease = 1;
		int currDecrease = 1;

		for (int i = 1; i < nums.size(); i++)
		{
			if (nums[i] > nums[i - 1])
			{
				currIncrease++;
				currDecrease = 1;
			}
			else if (nums[i] < nums[i - 1])
			{
				currDecrease++;
				currIncrease = 1;
			}
			else
			{
				currIncrease = 1;
				currDecrease = 1;
			}
			maxLength = max(maxLength, max(currIncrease, currDecrease));
		}

		return maxLength;
    }

	void test()
	{
		vector<int> v = { 1, 2, 2, 3, 4, 4, 5 };
		int result = longestMonotonicSubarray(v);
		Printer p;
		p.print(result);
	}
};
