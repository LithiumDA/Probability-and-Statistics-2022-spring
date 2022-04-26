import math
import random
import matplotlib.pyplot as plt

def get_chi2(n):
    x_list = [random.normalvariate(mu=0, sigma=1) for _ in range(n)]
    x2_list = [x*x for x in x_list]
    return sum(x2_list)

def get_t(n):
    # TODO: implement this function to sample a t(n) random variable
    # You may need to generate X, X_1, ..., X_n ~ i.i.d. N(0,1) first
    return 0

def get_F(n1, n2):
    # TODO: implement this function to sample an F(n1,n2) random variable
    # You may need to generate X_1, ..., X_n1, Y_1, ..., Y_n2 ~ i.i.d. N(0,1) first
    return 0

# This function plot histogram for the given list
def plot_histogram(x_list, distribution_name='', save_path=None):
    if save_path is None:
        save_path = distribution_name + '-histogram.pdf'
    plt.hist(x_list, bins=100)
    plt.title(f"Histogram of {distribution_name} distribution", fontsize=24)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=17)
    plt.savefig(save_path)
    plt.close()
    print(f"Histogram of {distribution_name} distribution has been generated")

if __name__ == '__main__':
    random.seed(1898)

    num_sample = 100000

    chi2_list = [get_chi2(5) for _ in range(num_sample)]
    plot_histogram(chi2_list, distribution_name='chi2(5)')

    t_list = [get_t(5) for _ in range(num_sample)]
    plot_histogram(t_list, distribution_name='t(5)')

    F_list = [get_F(3,5) for _ in range(num_sample)]
    plot_histogram(F_list, distribution_name='F(3,5)')