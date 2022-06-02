import numpy as np
import matplotlib.pyplot as plt

def get_data():
	x_list = [180, 104, 134, 141, 204, 150, 121, 151, 147, 145, 141, 144,
			  190, 190, 161, 165, 154, 116, 123, 151, 110, 108, 158, 107,
			  180, 127, 115, 191, 190, 153, 155, 177, 177, 143]
	y_list = [200, 100, 135, 125, 235, 170, 125, 135, 155, 165, 135, 160,
			  190, 210, 145, 195, 150, 100, 110, 180, 130, 110, 130, 115,
			  240, 135, 120, 205, 220, 145, 160, 185, 205, 160]
	return x_list, y_list

def linear_regression(x_data, y_data):
	# TODO: implement linear regression here
	alpha, beta = 0, 0
	return alpha, beta

def visualization(x_data, y_data, alpha, beta, save_path='visualization.pdf'):
	# original data
	plt.plot(x_data, y_data, 'ro', markersize=7, color='m')
	# pridiction of linear regression
	plt.plot(x_data, [alpha+beta*x for x in x_data], linewidth=5, color='blue')
	plt.title(f"Visualization of predictions", fontsize=24)
	plt.xticks(fontsize=22)
	plt.yticks(fontsize=22)
	plt.grid(linestyle='-.')
	plt.tight_layout()
	plt.savefig(save_path)
	plt.close()

def hypothesis_test():
	# TODO: calculate statistics for the hypothesis test here
	pass

if __name__ == '__main__':
	x_list, y_list = get_data()
	alpha, beta = linear_regression(x_list, y_list)
	visualization(x_list, y_list, alpha, beta)
	hypothesis_test()