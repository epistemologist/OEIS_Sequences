#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#include<omp.h>

typedef int32_t Matrix[4]; 

/*
We represent a 2x2 matrix as a length 4 array
[ v[0] v[1]
  v[2] v[3]
]
*/

void print_matrix(Matrix m) {
	printf("[[%d, %d], [%d, %d]]\n",
		m[0], m[1], m[2], m[3]
	);
}

// A <- B
void set_matrix(Matrix A, Matrix B) {
	for (int i = 0; i < 4; i++) A[i] = B[i];
}

// A = A (mod n)
void mat_mod(Matrix A, int n) {
	for (int i = 0; i < 4; i++) A[i] %= n;
}

// C = A+B
void mat_add(Matrix A, Matrix B, Matrix C) {
	for (int i = 0; i < 4; i++) {
		C[i] = A[i] + B[i];
	}
}

/*
[ a0 a1 ]  *  [ b0 b1 ]  = 
[ a2 a3 ]     [ b2 b3 ]

[  a0 b0 + a1 b2      a0 b1 + a1 b3  ]
[  a2 b0 + a3 b2      a2 b1 + a3 b3  ]   
*/

// C = AB
void mat_mul(Matrix A, Matrix B, Matrix C) {
	C[0] = A[0]*B[0] + A[1]*B[2];
	C[1] = A[0]*B[1] + A[1]*B[3];
	C[2] = A[2]*B[0] + A[3]*B[2];
	C[3] = A[2]*B[1] + A[3]*B[3];
}

// out = M^exp (mod m)
void mat_pow(
	Matrix M,
	int exp,
	int m,
	Matrix out
) {
	Matrix M_copy, tmp, res = {1, 0, 0, 1};
	set_matrix(M_copy, M);
	set_matrix(out, res);
	mat_mod(M, m);
	while (exp > 0) {
		if (exp & 1) {
			mat_mul(res, M_copy, tmp);
			mat_mod(tmp, m);
			set_matrix(res, tmp);
		}
		mat_mul(M_copy, M_copy, tmp);
		mat_mod(tmp, m);
		set_matrix(M_copy, tmp);
		exp >>= 1;
	}
	set_matrix(out, res);
}

bool is_ok(int n) {
	Matrix M = {0};
	Matrix tmp;	
	for (int a = 0; a < n; a++) {
		for (int b = 0; b < n; b++) {
			for (int d = 0; d < n; d++) {
				Matrix k = {a, d, d, b};
				mat_pow(k, n, n, tmp);
				mat_add(M, tmp, M);
				mat_mod(M, n);
			}
		}
	}
	return !(M[0] == 0 && M[1] == 0 && M[2] == 0 && M[3] == 0);
}

int main() {
	#pragma omp parallel for
	for (int i = 1000; i > 0; i--) {
		if (is_ok(i)) printf("%d\n", i);	
	}
}
