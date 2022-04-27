import math
import random

def get_D_n(n):
    # TODO: implement this function to sample D_n for a given n
    # You may need to generate X_1, ..., X_n ~ i.i.d. U(0,1) first and then compute D_n.
    return 0

if __name__ == '__main__':
    random.seed(1898)

    print(f"n\tDn\tln(n)Dn\tsqrt(n)Dn\tnDn")

    for n in [10**z for z in range(1,8)]:
        D_n = get_D_n(n)
        print(f"10^{math.log10(n):.0f}\t{D_n:.4f}\t{math.log(n)*D_n:.4f}\t{math.sqrt(n)*D_n:.4f}\t\t{n*D_n:.4f}")