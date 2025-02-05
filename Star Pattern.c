//
// Created by Anshumaan soni on 2/5/25.
//

#include <stdio.h>
void main() {
    for (int i = 1; i <=5; i++) {
        for (int j=1; j<=i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    for (int i = 4; i >=0; i--) {
        for (int j=1; j<=i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}