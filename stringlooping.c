//
// Created by Anshumaan soni on 2/19/25.
//

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char vowels[10]={'a','e','i','o','u','A','E','I','O','U'};

void len(char t[]) {
    int len=0,i=0;
    while (t[i]!='\0') {
        len++;
        i++;
    }
    printf("The length of the string is: %d",len);
}

void charac(char t[]) {
    int len=0,i=0;
    while (t[i]!='\0') {
        if (t[i]==' ' || t[i]=='\n') {
            continue;
        }
        else {
            len++;
        }
    }
    printf("No. of characters are : %d",len);
}

int check(char n) {
    int temp;
    for (int i=0;i<=9;i++) {
        if (n==vowels[i]) {
            temp++;
        }
        else {
            continue;
        }
        return temp;
    }
}

void vowel(char t[]) {
    int len=0,i=0;
    while (t[i]!='\0') {
        if (check(t[i])>0) {
            len++;
        }
        else {
            continue;
        }
    }
    printf("No. of Vowels are : %d",len);
}


void main() {
    char a[20];
    printf("Enter a string: ");
    //fgets(a,20,stdin);
    scanf("%s",a);
    len(a);
    charac(a);
    vowel(a);
}