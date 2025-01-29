//
// Created by Anshumaan soni on 1/29/25.
//

#include <stdio.h>

// Function to calculate the nth number in the Fibonacci series
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}

// Function to print the Fibonacci series up to nth number
void printFibonacci(int n) {
    printf("Fibonacci series up to %d:\n", n);
    for (int i = 0; i <= n; i++) {
        printf("%d ", fibonacci(i));
    }
}

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printFibonacci(n);

    return 0;
}
