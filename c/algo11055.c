#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    int n, ans = 0;
    int dp[1001] = {0, };
    char input[1001];

    fgets(input, 1001, stdin);

    char *ptr = strtok(input, " ");
    int idx = 0;

    while (ptr != NULL) {
        for (int i = 0 ; i < idx ; i++) {
            if (input[i] < input[idx]) {
                dp[idx] = max(dp[idx], dp[i]);
            }
        }

        dp[idx] += input[idx];
        ans = max(ans, dp[idx]);

        ptr = strtok(NULL, " "); idx++;
    }

    printf("%d", ans);
    return 0;
}