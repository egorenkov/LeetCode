#include <unordered_map>
#include<map>
using namespace std;



class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        map<int, int> my_map;
        int res = 0;
        int count = 0;
        my_map[0] = -1;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                count -= 1;
            }
            else {
                count += 1;
            }

            if (my_map.find(count) != my_map.end()) {
                res = max(res, i - my_map[count]);
            }
            else {
                my_map[count] = i;
            }
        }
        return res;
    }
};


/*
Когда count снова становится 0 (например, после [0, 1]), длина подмассива вычисляется как:
i - (-1) = i + 1 → корректно захватывает весь пройденный участок.

Операция	std::map	std::unordered_map (в среднем)
Вставка (insert)	O(log n)	O(1)
Поиск (find)	O(log n)	O(1)
Удаление (erase)	O(log n)	O(1)
Доступ ([])	O(log n)	O(1)

Используйте std::map, если:
Нужен отсортированный порядок ключей.
*/