//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

void Composite() {
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

void EvOd () {
    int a;
    printf("Enter a number: \n");
    scanf("%d", &a);
    if (a % 2 == 0) {
        printf("%d is an even number", a);
    }
    else {
        printf("%d is an odd number", a);
    }
}

void main() {
    int func;
    printf("Prime Coprime (1) \n"
        "Even Odd (2)\n");
    scanf("%d", &func);

    switch (func) {
        case 1:
            Composite();
            break;
        case 2:
            EvOd();
            break;
        default:
            printf("Invalid input");
            break;
    }
}

