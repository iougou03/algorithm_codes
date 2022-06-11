#include <iostream>
#include <vector>
#define MAX_LEN 100001
using namespace std;

int n, a, b;
vector<int> v[MAX_LEN];
int bfs_input[MAX_LEN];

int main() {
    cin >> n;
    for (int i = 0 ; i < n - 1 ; i++) {
        cin >> a >> b;

        v[a].push_back(b);
        v[b].push_back(a);
    }

    for (int i = 0 ; i < n ; i++) {
        cin >> a;
        bfs_input[i] = a;
    }

    cout << bfs_input;
    
    return 0;
}