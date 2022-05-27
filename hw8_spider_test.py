import pandas as pd
import numpy as np
import math
from scipy.stats import t

'''
This code shows to load data from the orginal file, hw8_spider.csv, and process the data
'''

# data input
file_location = "hw8_spider.csv"
data = pd.read_csv(file_location)

# remove unobserved data points
data=data.dropna()

# sort by group treatment
group_WF = data.loc[data["FOOD TREATMENT"]=="WF"]
group_LF = data.loc[data["FOOD TREATMENT"]=="LF"]
PWL_WF = group_WF["PREY WEIGHT LOSS"]
PWL_LF = group_LF["PREY WEIGHT LOSS"]

# calculate statsitics T
mean_WF = PWL_WF.mean()
mean_LF = PWL_LF.mean()
sampleVar_WF = PWL_WF.var()#sample variance S^2
sampleVar_LF = PWL_LF.var()
n_WF = len(PWL_WF)
n_LF = len(PWL_LF)
T = (mean_WF-mean_LF)/math.sqrt(sampleVar_WF/n_WF+sampleVar_LF/n_LF)

# calculate df
temp1 = sampleVar_WF/n_WF
temp2 = sampleVar_LF/n_LF
df=(temp1+temp2)**2/(temp1**2/(n_WF-1)+temp2**2/(n_LF-1))

# hypothesis test
alpha = 0.01
print(T>t.cdf(1-alpha,df))


'''
You can also write your own code, using the processed data.
Processed data can be loaded with the following code:
'''
# spider_WF = np.load('hw8_spider_WF.npy')
# spider_LF = np.load('hw8_spider_LF.npy')
