//
// Created by Anshumaan soni on 2/5/25.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char matrix[2][11] = {"Matrix1","Matrix2"};

typedef struct {
    int row1[2];
    int row2[2];
    char name[20];
} Matrix2D;

Matrix2D* Initmatrix(int row11, int row12, int row21, int row22, char name) {
    Matrix2D* newmat = (Matrix2D*)malloc(sizeof(Matrix2D));
    if (newmat == NULL) {
        perror("Matrix Inititation Failed");
        exit(EXIT_FAILURE);
    }
    newmat->row1[0] = row11;
    newmat->row1[1] = row12;
    newmat->row2[0] = row21;
    newmat->row2[1] = row22;
    strcpy(newmat->name,name);
}

void matdef() {
    Matrix2D matrix;
    int a;
    for (int i = 0; i < 2; i++) {
        if (i==0) {
            for (int j = 0; j < 2; j++) {
                printf("Enter Value for position %d:%d : ",(i+1),(j+1));
                scanf("%d", &a);
                matrix.row1[j] = a;
            }
        }
        else if (i==1) {
            for (int j = 0; j < 2; j++) {
                printf("Enter Value for position %d:%d : ",(i+1),(j+1));
                scanf("%d", &a);
                matrix.row2[j] = a;
            }
        }
    }
    for (int i = 0; i < 2; i++) {
        if (i==0) {
            printf("Row %d : \n",(i+1));
            for (int j = 0; j < 2; j++) {
                printf("%d ", matrix.row1[j]);
            }
        }
        else if (i==1) {
            printf("Row %d : \n",(i+1));
            for (int j = 0; j < 2; j++) {
                printf("%d ", matrix.row2[j]);
            }
        }
        printf("\n");
    }
}

int main() {
    for (int n = 0; n <= 1; n++) {
        printf("Enter the Data for %s\n", matrix[n]);
        matdef();
    }
    return 0;
}