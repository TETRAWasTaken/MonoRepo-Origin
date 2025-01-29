//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

void main () {
    int n,f=1;
    printf("Enter a factorial No. : \n");
    scanf("%d", &n);

    for (int i = 1; i <= n ; i++ )
    f = f * i;

    printf("The Factorial of the Number is : %d",f);
}