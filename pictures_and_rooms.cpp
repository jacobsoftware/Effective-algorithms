#include <iostream>
#include <vector>
 
using namespace std;
 
int ppl_in_rooms(vector<int>& rooms, int n) {
    vector<int> list_of_ppl(n, 1);
    int non_empty_rooms = 0;
    vector<int> prev_list;
 
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (list_of_ppl[j] > 0) {
                list_of_ppl[j]--;
                list_of_ppl[rooms[j] - 1]++;
            }
        }
 
        if (prev_list == list_of_ppl) {
            break;
        } else {
            prev_list = list_of_ppl;
        }
    }
 
    for (int i = 0; i < n; ++i) {
        if (list_of_ppl[i] > 0) {
            non_empty_rooms++;
        }
    }
 
    return non_empty_rooms;
}
 
int main() {
    int data_sets;
    cin >> data_sets;
    vector<int> results;
 
    for (int i = 0; i < data_sets; ++i) {
        int n;
        cin >> n;
        vector<int> rooms(n);
 
        for (int j = 0; j < n; ++j) {
            cin >> rooms[j];
        }
 
        results.push_back(ppl_in_rooms(rooms, n));
    }
 
    for (int result : results) {
        cout << result << endl;
    }
 
    return 0;
}