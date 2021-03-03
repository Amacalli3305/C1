
#Clase 1: Profesor.
#03/03/21
import pandas as pd
import numpy as np
import matplotlib as mpl
import scipy
import importlib 
import matplotlib.pylab as plt
from scipy.stats import skew, kurtosis, chi2

nb_sim = 10**6
df = 3
dist_name = 'chi square' # Student normal exponential uniform chi square
if dist_name == 'normal':
 x = np.random.standard_normal(nb_sim)
 x_str = dist_name
elif dist_name == 'exponential':
 x= np.random.standard_exponential(nb_sim)
 x_str = dist_name
elif dist_name =='uniform':   
 x = np.random.uniform(0,1,nb_sim)
 x_str = dist_name
elif dist_name == 'student': 
 x = np.random.standard_t(df = df, size=nb_sim)
 x_str = dist_name + ' / df = ' + str(df)
elif dist_name == 'chi square':
    x = np.random.chisquare(df = df, size = nb_sim)
    x_str = dist_name + ' / df = ' + str(df)

#Plot histogram
plt.figure()
plt.hist(x, bins = 100)
plt.title(x_str)
plt.show
//