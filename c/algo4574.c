#include <stdio.h>

int COMPLETE = 0;
int sudominku_grid[10][10] = {0, };
int comb_set[10][10] = {0, };

int* get_coor(char* coor) {
    int y = (int)coor[0] - (int)"A" + 1;
    int x = (int)coor[1];

    int result[2] = { x, y };

    return result;
}

int main() {
    int T;
    int U, V;
    char LU[2], LV[2];

    while(1) {
        scanf("%d", &T);
        if(T == 0) break;

        COMPLETE = 0;

        for(int i = 0 ; i < T ; i++) {
            scanf("%d %c%c %d %c%c",&U, LU, &V, LV);
            // get_coor()
            printf("%d %s %d %s",U, LU, V, LV);
        }

        for(int i = 0 ; i < 9 ; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
        }
    }


    return 0;
}