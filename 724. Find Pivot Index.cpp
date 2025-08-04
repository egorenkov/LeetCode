#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int totalsum = 0;
        for (int i = 0; i < n; i++) {
            totalsum += nums[i];
        }
        int left = 0;
        for (int i = 0; i < n; i++) {
            if (2 * left + nums[i] == totalsum) {
                return i;
            }
            left += nums[i];
        }

        return -1;

    }
};