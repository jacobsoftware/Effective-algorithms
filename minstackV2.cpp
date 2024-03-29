#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> stack_of_values;
    std::vector<int> results;

    for (int i = 0; i < n; ++i) {
        std::string action;
        std::cin >> action;

        if (action == "PUSH") {
            int value;
            std::cin >> value;
            stack_of_values.push_back(value);
        } else if (action == "POP") {
            stack_of_values.pop_back();
        } else if (action == "MIN") {
            results.push_back(*std::min_element(stack_of_values.begin(), stack_of_values.end()));
        }
    }

    for (const auto& result : results) {
        std::cout << result << std::endl;
    }

    return 0;
}
