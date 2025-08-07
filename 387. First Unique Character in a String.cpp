class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> vec(26);
        for (const char& el : s) {
            vec[el - 'a'] += 1;
        }
        for (int i = 0; i < s.size(); i++) {
            if (vec[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
};