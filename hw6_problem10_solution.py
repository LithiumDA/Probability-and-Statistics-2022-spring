import math
import random

def get_D_n(n):
    x_list = [random.random() for _ in range(n)] # generate X_1, ..., X_n ~ i.i.d. U(0,1)
    x_list.sort() # sort X_i's to obtain X_(1), ..., X_(n)
    discrepancy = [abs((i+1)/n - x_list[i]) for i in range(n)]
    return max(discrepancy)

if __name__ == '__main__':
    random.seed(1898)
    print(f"n\tDn\tln(n)Dn\tsqrt(n)Dn\tnDn")
    for n in [10**z for z in range(1,8)]:
        D_n = get_D_n(n)
        print(f"10^{math.log10(n):.0f}\t{D_n:.4f}\t{math.log(n)*D_n:.4f}\t{math.sqrt(n)*D_n:.4f}\t\t{n*D_n:.4f}")
