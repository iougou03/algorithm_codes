#include <stdio.h>
#define MAX_LEN 100001

int edges[MAX_LEN][MAX_LEN] = {0, };


int check_bfs_valid(int* bfs_arr) {

}

int main () {
    int n, x, y;
    char input[200001] = "";

    scanf("%d", &n);

    for(int i = 0 ; i < n - 1 ; i++) {
        scanf("%d %d ", &x, &y);

        edges[x][y] = 1;
        edges[y][x] = 1;
    }

	fgets(input, n * 2, stdin);

    printf("%s", input);
    // check_bfs_valid
    
    return 0;
}