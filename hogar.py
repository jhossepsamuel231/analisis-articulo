import numpy as np
from scipy import stats
from scipy.stats import t
import matplotlib.pyplot as plt

asis = [7.74, 8.58, 8.01, 7.72, 7.12, 8.23, 7.19, 9.46, 9.82, 6.92, 8.96, 7.64, 7.84, 
        9.63, 5.36, 5.44, 5.10, 9.16, 8.89, 9.35, 9.89, 8.99, 7.31, 8.90, 5.59, 8.20, 
        5.72, 9.72, 7.61, 7.07, 6.32, 8.87, 7.28, 7.84, 5.09, 8.09, 8.06, 8.08, 9.72, 
        8.41, 6.80, 7.19, 8.49, 5.30, 8.33, 8.35, 6.05, 5.64, 6.58, 6.82, 7.85, 7.19, 
        9.94, 5.51, 6.04, 5.81, 8.27, 6.27, 7.33, 6.22, 5.79, 5.55, 8.28, 5.69, 5.98, 
        6.84, 9.10, 5.49, 9.19, 5.48, 9.88, 7.34, 9.88, 8.02, 8.70, 5.20, 6.41, 5.60, 
        6.48, 5.59, 6.59, 7.07, 5.32, 8.46, 7.83, 6.33, 7.62, 5.47, 7.88, 9.65, 6.59, 
        8.34, 5.66, 8.58, 6.45, 5.92, 7.93, 5.10, 9.14, 5.02, 8.39, 6.35, 8.68, 9.81, 
        6.24, 7.88, 7.96, 7.86, 6.12, 9.76, 7.24, 9.23, 8.50, 6.49, 9.07, 6.98, 9.41, 
        7.91, 9.41, 8.46, 8.63, 7.51, 9.78, 8.22, 7.12, 8.03, 5.10, 6.51, 8.30, 6.45, 
        8.09, 7.14, 5.68, 6.49, 7.85, 7.95, 7.87, 8.27, 8.26, 7.16, 9.48, 6.84, 7.18, 
        9.46, 9.03, 8.52, 5.50, 9.60, 8.57, 9.99, 5.75, 9.34, 5.81, 8.08, 5.62, 9.24, 
        9.04, 7.85, 7.04, 5.35, 8.49, 7.27, 8.61, 9.33, 9.88, 9.28, 5.06, 6.80, 8.65, 
        5.86, 7.61, 5.27, 6.00, 5.09, 8.97, 6.12, 6.73, 9.64, 8.52, 5.16, 5.82, 8.11, 
        7.89, 6.19, 9.67, 8.07, 7.68, 7.95, 8.65, 6.56, 6.99, 6.05, 5.93, 9.72, 8.70, 
        7.45, 6.14, 6.27, 5.29, 7.17]
tobe = [5.61, 7.72, 4.40, 7.78, 7.48, 5.82, 5.31, 4.93, 6.46, 4.13, 4.06, 5.72, 4.27, 
        5.01, 4.88, 5.01, 4.52, 4.05, 4.46, 6.47, 7.90, 7.96, 5.64, 4.65, 6.56, 5.96, 
        7.96, 4.26, 7.13, 5.15, 4.97, 6.65, 4.98, 6.66, 6.07, 5.70, 6.22, 5.15, 6.83, 
        5.66, 5.44, 7.31, 7.70, 4.18, 4.93, 5.39, 7.26, 7.94, 7.88, 7.62, 5.19, 7.97, 
        5.00, 4.42, 7.80, 4.93, 6.76, 4.23, 6.92, 7.53, 5.09, 5.52, 5.50, 7.00, 4.95, 
        4.69, 5.80, 5.22, 7.36, 4.95, 6.01, 7.77, 6.54, 7.47, 7.76, 7.00, 6.80, 7.87, 
        7.98, 5.81, 4.28, 5.17, 4.61, 5.67, 4.53, 6.42, 5.53, 7.58, 7.87, 6.19, 5.10, 
        6.37, 7.59, 5.63, 6.21, 5.09, 5.82, 5.61, 4.99, 6.02, 5.24, 5.49, 6.10, 7.00, 
        5.33, 7.70, 7.45, 4.19, 5.01, 5.78, 4.42, 5.39, 6.96, 6.72, 6.49, 6.84, 4.82, 
        5.37, 6.70, 7.52, 6.17, 5.13, 4.12, 6.84, 4.03, 5.49, 6.12, 7.69, 4.36, 5.62, 
        4.10, 5.37, 6.49, 5.12, 4.84, 4.46, 6.31, 6.78, 6.69, 7.80, 4.01, 6.59, 6.40, 
        6.35, 7.85, 4.07, 6.79, 7.25, 6.04, 5.34, 7.16, 4.39, 5.77, 6.08, 6.78, 4.36, 
        4.91, 5.64, 6.49, 7.55, 6.48, 4.53, 7.92, 7.49, 6.01, 7.69, 6.17, 7.69, 7.32, 
        7.87, 7.68, 4.14, 4.70, 5.56, 7.81, 5.20, 4.64, 7.55, 5.79, 7.63, 4.64, 6.64, 
        5.76, 4.31, 6.79, 4.99, 4.16, 4.24, 4.24, 7.63, 6.96, 7.59, 6.69, 6.12, 5.22, 
        7.99, 5.45, 5.88, 5.51, 7.92]

promedio_asis = np.mean(asis)
promedio_tobe = np.mean(tobe)

print("------------------------------------------------------------------------------")
print("Tiempo promedio de búsqueda As-Is: ", promedio_asis)
print("Tiempo promedio de búsqueda To-Be: ", promedio_tobe)

# Realizar la prueba de hipótesis
t_stat, p_value = stats.ttest_ind(asis, tobe, equal_var=False)

print("Valor t calculado: ", t_stat)
print("Valor p:", p_value)

alpha = 0.05

# Calcular los grados de libertad
n1 = len(asis)
n2 = len(tobe)
df = n1 + n2 - 2

# Calcular el valor crítico de t
t_critical = t.ppf(1 - alpha/2, df)

print("valor critio Tc: ", t_critical)

if p_value < alpha:
    print("Se rechaza la hipótesis nula. Hay evidencia suficiente para decir que el tiempo promedio de búsqueda de trabajo en hogar ha disminuido significativamente.")
else:
    print("No se puede rechazar la hipótesis nula. No hay suficiente evidencia para afirmar que el tiempo promedio de búsqueda de trabajo en hogar ha disminuido significativamente.")

print("------------------------------------------------------------------------------")