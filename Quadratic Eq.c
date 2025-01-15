//
// Created by Anshumaan soni on 1/15/25.
//
#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c, discriminant, root1, root2, realpart, imagpart;
    printf("Enter the values of a, b and c: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("The roots are %lf and %lf\n", root1, root2);
    } else if (discriminant == 0) {
        root1 = root2 = -b / (2 * a);
        printf("The root is %lf\n", root1);
    }
    else {
        realpart = -b / (2 * a);
        imagpart = sqrt(-discriminant) / (2 * a);
        printf("The roots are %lf + %lfi and %lf + %lfi\n", realpart, imagpart, realpart, -imagpart);
    }
    return 0;
}