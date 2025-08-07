class Solution {
public:
    string defangIPaddr(string address) {
        string res = "";
        for (char s : address) {
            if (s == '.') {
                res += "[.]";
            }
            else {
                res += s;
            }

        }
        return res;
    }
};