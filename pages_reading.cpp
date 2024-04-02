#include <iostream>
#include <vector>
using namespace std;

bool contains_one(const vector<int>& pages) {
    for (int page : pages) {
        if (page == 1)
            return true;
    }
    return false;
}

int pages_reading(vector<int>& pages, int n) {
    int rounds = 0;
    if (!contains_one(pages)) return rounds;

    for (int i = 0; i < n; ++i) {
        if (pages[0] == 1 && i == 0) {
            for (int j = 0; j < n; ++j) {
                if (pages[j] == 1)
                    pages[j] = 0;
                else
                    pages[j] = 1;
            }
            rounds += 1;
        }
        else {
            pages.erase(pages.begin());
            for (int j = 0; j < n - 1; ++j) {
                if (j == 0 && pages[j] == 1) {
                    pages[0] = 0;
                } else if (j == 0 && pages[j] == 0) {
                    break;
                }
                if (j != 0 && pages[j] == 1) {
                    pages[j] = 0;
                } else if (j != 0 && pages[j] == 0) {
                    pages[j] = 1;
                }
            }
            pages.push_back(0);
            rounds += 1;
            if (!contains_one(pages)) return rounds;
        }
    }

    if (contains_one(pages)) return -1;  // 'NIGDY'
    else return rounds;
}

int main() {
    int data_sets;
    cin >> data_sets;
    vector<int> results(data_sets);
    
    for (int i = 0; i < data_sets; ++i) {
        int n;
        cin >> n;
        vector<int> pages(n);
        for (int j = 0; j < n; ++j)
            cin >> pages[j];
        results[i] = pages_reading(pages, n);
    }
    
    for (int i = 0; i < data_sets; ++i) {
        if (results[i] == -1)
            cout << "NIGDY" << endl;
        else
            cout << results[i] << endl;
    }

    return 0;
}
