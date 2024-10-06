#include <vector>
#include <tuple>
using namespace std;

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size();
		int n = img[0].size();

		vector<vector<int>> res(m, vector<int>(n, 0));

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				vector<tuple<int, int>> neighbours = getNeighbours(i, j, m, n);
				int sum = 0;
				int count = 0;
				for (auto neighbour : neighbours) {
					int x = get<0>(neighbour);
					int y = get<1>(neighbour);
					sum += img[x][y];
					count++;
				}
				// get floor of the average
				res[i][j] = sum / count;
			}
		}

		return res;
    }

	vector<tuple<int, int>> getNeighbours(int i, int j, int m, int n) {
		vector<tuple<int, int>> neighbours;

		for (int x = i - 1; x <= i + 1; x++) {
			if (x < 0 || x >= m) {
				continue;
			}
			for (int y = j - 1; y <= j + 1; y++) {
				if (y < 0 || y >= n) {
					continue;
				}

				neighbours.push_back(make_tuple(x, y));
			}
		}
		
		return neighbours;
	}
};