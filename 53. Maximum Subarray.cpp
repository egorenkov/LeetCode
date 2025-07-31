﻿

#include <iostream>
#include <vector>


class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int sum = 0, maxsum = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (sum > maxsum) {
                maxsum = max(sum, maxsum);
            }
            if (sum < 0) {
                sum = 0;
            }
        }
        return maxsum;
    }
};

int main()
{

}
