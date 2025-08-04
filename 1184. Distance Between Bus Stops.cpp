class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int from_start_to_destination = 0;
        int from_destination_to_start = 0;


        int n = distance.size();
        int i = start;

        while (i != destination) {
            from_start_to_destination += distance[i];
            i = (i + 1) % n;
        }

        int j = destination;
        while (j != start) {
            from_destination_to_start += distance[j];
            j = (j + 1) % n;
        }
        return min(from_destination_to_start, from_start_to_destination);
    }
};