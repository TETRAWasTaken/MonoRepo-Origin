//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

int CW1() {
    double number, sum = 0;

    do {
        printf("Enter a number: ");
        scanf("%lf", &number);
        sum+=number;
    }
    while (number != 0.0);
    printf("The sum is: %lf", sum);
    return 0;
}

void CW2() {

}


void main() {
    // CW1();
}
