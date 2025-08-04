class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN, max4 = INT_MIN;
        int max5 = INT_MIN, max6 = INT_MIN, max7 = INT_MIN, max8 = INT_MIN;
        int min1 = INT_MAX, min2 = INT_MAX, min3 = INT_MAX, min4 = INT_MAX;
        int min5 = INT_MAX, min6 = INT_MAX, min7 = INT_MAX, min8 = INT_MAX;

        for (int i = 0; i < n; ++i) {
            // Combination 1: arr1[i] + arr2[i] + i
            int val1 = arr1[i] + arr2[i] + i;
            max1 = max(max1, val1);
            min1 = min(min1, val1);

            // Combination 2: arr1[i] + arr2[i] - i
            int val2 = arr1[i] + arr2[i] - i;
            max2 = max(max2, val2);
            min2 = min(min2, val2);

            // Combination 3: arr1[i] - arr2[i] + i
            int val3 = arr1[i] - arr2[i] + i;
            max3 = max(max3, val3);
            min3 = min(min3, val3);

            // Combination 4: arr1[i] - arr2[i] - i
            int val4 = arr1[i] - arr2[i] - i;
            max4 = max(max4, val4);
            min4 = min(min4, val4);

            // Combination 5: -arr1[i] + arr2[i] + i
            int val5 = -arr1[i] + arr2[i] + i;
            max5 = max(max5, val5);
            min5 = min(min5, val5);

            // Combination 6: -arr1[i] + arr2[i] - i
            int val6 = -arr1[i] + arr2[i] - i;
            max6 = max(max6, val6);
            min6 = min(min6, val6);

            // Combination 7: -arr1[i] - arr2[i] + i
            int val7 = -arr1[i] - arr2[i] + i;
            max7 = max(max7, val7);
            min7 = min(min7, val7);

            // Combination 8: -arr1[i] - arr2[i] - i
            int val8 = -arr1[i] - arr2[i] - i;
            max8 = max(max8, val8);
            min8 = min(min8, val8);
        }

        int res = 0;
        res = max(res, max1 - min1);
        res = max(res, max2 - min2);
        res = max(res, max3 - min3);
        res = max(res, max4 - min4);
        res = max(res, max5 - min5);
        res = max(res, max6 - min6);
        res = max(res, max7 - min7);
        res = max(res, max8 - min8);

        return res;
    }
};