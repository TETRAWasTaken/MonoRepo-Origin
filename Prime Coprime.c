//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

void main () {
    int a, temp=0;
    printf("Enter a number: \n");
    scanf("%d", &a);

    for (int i = 2; i <= a/2; i++) {
        if (a % i == 0) {
            temp++;
        }
        else {
            continue;
        }
    }
    if (temp > 0) {
        printf("%d is not a prime number", a);
    }
    else {
        printf("%d is a prime number", a);
    }
}