#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int min_steps_to_sort_cards(vector<int>& cards, int n) {
    vector<int> card_positions(n + 1, 0);
    vector<int> lis(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (cards[i] > cards[j]) {
                lis[i] = max(lis[i], lis[j] + 1);
            }
        }
    }

    int min_steps = n - *max_element(lis.begin(), lis.end());
    return min_steps;
}

int main() {
    int data_sets;
    cin >> data_sets;
    vector<int> results(data_sets);

    for (int i = 0; i < data_sets; ++i) {
        int n;
        cin >> n;
        vector<int> cards(n);
        for (int j = 0; j < n; ++j) {
            cin >> cards[j];
        }
        results[i] = min_steps_to_sort_cards(cards, n);
    }

    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}
