class Solution {
public:
    char repeatedCharacter(string s) {
        vector<int> vec(26);
        for (int i = 0; i < s.size(); i++) {
            vec[s[i] - 'a'] += 1;
            if (vec[s[i] - 'a'] == 2) {
                return s[i];
            }
        }
        return ' ';
    }
};