#include <stdio.h>

int sum(int* arr, int start, int end) {
    int sum = 0;

    for (int i = start ; i < end ; i++){
        sum += arr[i];
    }

    return sum;
}

int main() {
    int n, s;
    int top = 0, bottom = 0;
    int seq[100000];
    int ans = 100000;

    scanf("%d %d", &n, &s);

    for (int i = 0 ; i < n ; i++) {
        scanf("%d", &seq[i]);
    }

    while (top <= bottom && bottom <= n) {
        if (sum(seq, top, bottom) < s) {
            bottom++;
        } else {
            ans = (ans > bottom - top) ? bottom - top : ans;
            top += 1;
        }
    }  

    printf("%d\n", ans);
    return 0;
}