//
//  main.c
//  AdventOfCode
//
//  Created by Lukas Görtz on 06.12.22.
//

#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX 4100
int main(int argc, char **argv){
    char st[MAX];
    int whichSt = 1;
    while (scanf("%s",st)!= EOF) {
        printf("Part 1:\n");
        for (int i = 0; i < strlen(st)-4; i++) {
            if(st[i] != st[i+1] && st[i] != st[i+2] && st[i] != st[i+3]
               && st[i+1] != st[i+2] && st[i+1] != st[i+3]
               && st[i+2] != st[i+3]) {
                printf("Packet %d marker after %d\n",whichSt, i+4);
                i = MAX;
            }
        }
        printf("Part 2:\n");
        char st2[15];
        char temp;
        for (int x = 0; x < strlen(st)-4; x++) {
            memcpy(st2, &st[x], 14 );
            st2[14] = '\0';
            for(int i = 0; i<strlen(st2);i++){
                for(int j = i+1;j<strlen(st2);j++){
                    if(st2[i] > st2[j]){
                        temp = st2[i];
                        st2[i] = st2[j];
                        st2[j] = temp;
                    }
                }
            }
            int allUnique = 1;
            for(int k = 0; k < strlen(st2)-1; k++){
                if(st2[k] == st2[k+1]) {
                    k = MAX;
                    allUnique = 0;
                }
            }
            if(allUnique) {
                printf("Message %d marker after %d\n", whichSt, x+14);
                x = MAX;
            }
        }
        whichSt++;
    }
}
