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

Matrix2D* Initmatrix(int row11, int row12, int row21, int row22, char* name1) {
    Matrix2D* newmat = (Matrix2D*)malloc(sizeof(Matrix2D));
    if (newmat == NULL) {
        perror("Matrix Inititation Failed");
        exit(EXIT_FAILURE);
    }
    newmat->row1[0] = row11;
    newmat->row1[1] = row12;
    newmat->row2[0] = row21;
    newmat->row2[1] = row22;
    strcpy(newmat->name,name1);
    return newmat;
}

void freeMatrix(Matrix2D* mat) {
    if (mat != NULL) {
        free(mat);
        mat= NULL;
    }
}

void matrixrepresentation(Matrix2D* mat) {
    printf("⌈ %d %d ⌉\n",mat->row1[0],mat->row1[1]);
    printf("⌊ %d %d ⌋\n " ,mat->row2[0],mat->row2[1]);
}

void matdef(Matrix2D* matrix) {
    int a;
    for (int i = 0; i < 2; i++) {
        if (i==0) {
            for (int j = 0; j < 2; j++) {
                printf("Enter Value for position %d:%d : ",(i+1),(j+1));
                scanf("%d", &a);
                matrix->row1[j] = a;
            }
        }
        else if (i==1) {
            for (int j = 0; j < 2; j++) {
                printf("Enter Value for position %d:%d : ",(i+1),(j+1));
                scanf("%d", &a);
                matrix->row2[j] = a;
            }
        }
    }
    matrixrepresentation(matrix);
}

void Addition(Matrix2D* mat1, Matrix2D* mat2) {
    Matrix2D tempmat;
    tempmat.row1[0] = mat1->row1[0] + mat2->row1[0];
    tempmat.row1[1] = mat1->row1[1] + mat2->row1[1];
    tempmat.row2[0] = mat1->row2[0] + mat2->row2[0];
    tempmat.row2[1] = mat1->row2[1] + mat2->row2[1];

    matrixrepresentation(&tempmat);
}

void Substraction(Matrix2D* mat1, Matrix2D* mat2) {
    Matrix2D tempmat;
    tempmat.row1[0] = mat1->row1[0] - mat2->row1[0];
    tempmat.row1[1] = mat1->row1[1] - mat2->row1[1];
    tempmat.row2[0] = mat1->row2[0] - mat2->row2[0];
    tempmat.row2[1] = mat1->row2[1] - mat2->row2[1];

    matrixrepresentation(&tempmat);
}

void Multiplication(Matrix2D* mat1, Matrix2D* mat2) {
    Matrix2D tempmat;
    tempmat.row1[0] = mat1->row1[0]*mat2->row1[0] + mat1->row1[1]*mat2->row2[0];
    tempmat.row1[1] = mat1->row1[0]*mat2->row1[1] + mat1->row1[1]*mat2->row2[1];
    tempmat.row2[0] = mat1->row2[0]*mat2->row1[0] + mat1->row2[1]*mat2->row2[0];
    tempmat.row2[1] = mat1->row2[0]*mat2->row1[1] + mat1->row2[1]*mat2->row2[1];

    matrixrepresentation(&tempmat);
}

void function(Matrix2D* mat1, Matrix2D* mat2) {
    int n;
    printf("What Function Do you want to perform : \n"
           "-> Addition (1)\n"
           "-> Subtraction (2)\n"
           "-> Multiplication (3)\n ");

    for (int i = 0; i < 3; i++) {
        printf("Enter Operator - \n");
        scanf("%d",&n);
        if (n==1) {
            Addition(mat1, mat2);
        }
        else if (n==2) {
            Substraction(mat1, mat2);
            continue;
        }
        else if (n==3) {
            Multiplication(mat1, mat2);
            continue;
        }
        else {
            printf("Wrong Input\n");
        }
    }
}

int main() {
    Matrix2D* matrix1 = Initmatrix(0,0,0,0,"Matrix1");
    Matrix2D* matrix2 = Initmatrix(0,0,0,0,"Matrix2");
    printf("Enter the Data for Matrix 1\n");
    matdef(matrix1);
    printf("Enter the Data for Matrix 2\n");
    matdef(matrix2);

    function(matrix1,matrix2);

    freeMatrix(matrix1);
    freeMatrix(matrix2);
    return 0;
}