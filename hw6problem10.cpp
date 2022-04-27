#include <bits/stdc++.h>

double sample_uniform(double low, double high){
    /* Helper function: sample a random variable from U(low,high) distribution. */
    return ((double) rand() / RAND_MAX) * (high-low) + low;
}

double get_D_n(int n){
    // TODO: implement this function to sample D_n for a given n
    // You may need to generate X_1, ..., X_n ~ i.i.d. U(0,1) first and then compute D_n.
    return 0;
}

int main(){
    srand(1898);

    printf("n\tDn\tln(n)Dn\tsqrt(n)Dn\tnDn\n");
    for (int i=1,n=10; i<8; ++i,n*=10){
        double D_n = get_D_n(n);
        printf("10^%d\t%.4f\t%.4f\t%.4f\t\t%.4f\n", 
                i, D_n, log(n)*D_n, sqrt(n)*D_n, n*D_n);
    }
    return 0;
}