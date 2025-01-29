//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

void fibionacci(int n) {
    if (n==0) {
        printf("Not Possible dumbass");
    }
    else if (n>1) {
        int a = 0, b = 1, c;
        for ( int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
            printf("%d\n", c);
        }
    }
}

void main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d\n",1);
    fibionacci(n);
}