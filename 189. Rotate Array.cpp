class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = nums.size() - k % nums.size();
        int n = k;
        vector<int> copy = nums;
        int ind = 0;
        for(; k < nums.size(); k++){
            nums[ind] = copy[k];
            ind += 1;
        }
        for(int j = 0; j < n;j++){
            nums[ind] = copy[j];
            ind += 1;
        }
    
    }
};