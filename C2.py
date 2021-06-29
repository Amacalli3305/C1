#Clase 2: Profesor
#Jarque-Bera
#05/03/21

import pandas as pd
import numpy as np
import matplotlib as mpl
import scipy
import importlib 
import matplotlib.pylab as plt
from scipy.stats import skew, kurtosis, chi2

#Prueba de Jarque-Bera: Normalidad 
#T-student, los grados de libertad a infinito se distribuye a una normal

nb_sim = 10**6
df = 100000
dist_name = 'student' # Student normal exponential uniform chi square
dist_type = 'simulated RV' #Simulando una variable aletoria, random variable

#Real: Datos reales
#Custom: Castear. Forzar a que otra variable sea distinta.
#Enteros a Float.
#str(df)

if dist_name == 'normal':
 x = np.random.standard_normal(nb_sim)
 x_description = dist_type + ' ' + dist_name
elif dist_name == 'exponential':
 x= np.random.standard_exponential(nb_sim)
 x_description = dist_type + ' ' + dist_name
elif dist_name =='uniform':   
 x = np.random.uniform(0,1,nb_sim)
 x_description = dist_type + ' ' + dist_name
elif dist_name == 'student': 
 x = np.random.standard_t(df = df, size=nb_sim)
 x_description = dist_type + ' ' + dist_name + ' / df = ' + str(df)
elif dist_name == 'chi square':
    x = np.random.chisquare(df = df, size = nb_sim)
    x_description = dist_type + ' ' + dist_name +' / df = ' + str(df)

'''
Goal: Create a Jarque-Bera normality test


1. Necesitamos Kurtosis: Momento de orden 3
Colas pesadas mayores a tres
Colas ligeras menores a tres


2. Necesitamos skewenes(asimetría): Momento de orden 3
v.a normal tiene una skweness de cero
Momentos impares es cero

3.H0: Se distribuye normal
Deben de ser cero en exceso la kurtosis y la skwens, para que sea normal
si son grandes te alejas de la normalidad

4. Encontrar el umbral a partir de que número grande ya es normal
Asinoticamente el test JB se comporta como una chi2 con 2 grados de libertad
Cerca de cero en el eje x
K = 2, cerca de 0.5. Gráfica


5. P-VALUE: PASAR O NO EL TEST 
La probalidad de encontrar resultados tan extremos
 (valores de la derecha, positivos)
Probabilidad condicional: 
    Encontrar valores extremos dado que la distribución es normal
MAL: Proba de que sea normal dado el valor que obtuve

'''
x_mean = np.mean(x)
x_std = np.std(x)
x_skew= skew(x)
x_kurtosis = kurtosis(x) #Kurtosis en exceso k-3
x_jb_stat = nb_sim/6*(x_skew**2+1/4*x_kurtosis**2) 
#Que tan lejos estas de la normalidad
#Necesariamente chico
p_value = 1-chi2.cdf(x_jb_stat,df = 2)
#Se distribuye chi2 con 2 grados de libertad
#Si valor–p < nivel de significación => Rechazo H0. 
#Si valor–p > nivel de significación => No rechazo H0. 
x_is_normal = (p_value >0.05) #equivalente a jb <6

print ('skewness is ' + str(x_skew))
print ('kurtosis is ' + str(x_kurtosis))
print ('Jarque-Bera statistic is ' + str(x_jb_stat))
print ('p-value is ' + str(p_value))
print ('is normal ' + str(x_is_normal))


#jb_list = []
#jb_list.appennd(x_jb_stat)

#Plot histogram
plt.figure()
plt.hist(x, bins = 100)
plt.title(x_description)
plt.show


