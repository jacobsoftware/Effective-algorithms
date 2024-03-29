#include <iostream>
#include <cstdio>
#include <stack>
#include <utility>

using namespace std;

int Q;
int value;
char type[10];
stack<pair<int, int>> minStack;

int main(int argc, const char * argv[]) {
    scanf("%d", &Q); getchar();
    while (Q --) {
        scanf("%s", type);
        if (type[1] == 'U') { // PUSH
            scanf("%d", &value);
            minStack.push(make_pair(value, minStack.empty() ? value: min(minStack.top().second, value)));
        } else if (type[1] == 'O') { // POP
            if (minStack.empty()) {
                puts("EMPTY");
            } else {
                minStack.pop();
            }
        }
        else { // MIN
            if (minStack.empty()) {
                puts("EMPTY");
            } else {
                printf("%d\n", minStack.top().second);
            }
        }
    }
    
    return 0;
}