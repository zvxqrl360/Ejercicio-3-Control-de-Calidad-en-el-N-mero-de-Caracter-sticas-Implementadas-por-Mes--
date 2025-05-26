import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos: cada mes tiene dos observaciones (A y B)
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre'],
    'A':    [8, 10, 7, 12, 9, 10, 11, 8, 7, 10],
    'B':    [6.8, 10.8, 4.8, 9.2, 8.8, 10.8, 9.2, 6.8, 4.8, 9.2]
}

df = pd.DataFrame(data)

# Cálculo del promedio por mes (para gráfico X-barra)
df['Promedio'] = df[['A', 'B']].mean(axis=1)
media = df['Promedio'].mean()
desviacion = df['Promedio'].std(ddof=1)

# Límites de control para X-barra
UCL_x = media + 3 * desviacion
LCL_x = media - 3 * desviacion

# Cálculo del rango por mes (para gráfico R)
df['Rango'] = abs(df['A'] - df['B'])
media_r = df['Rango'].mean()

# Constantes para subgrupos de tamaño 2
D3 = 0
D4 = 3.267
UCL_r = D4 * media_r
LCL_r = D3 * media_r

# Crear gráficos lado a lado
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico X-barra
axs[0].plot(df['Mes'], df['Promedio'], marker='o', linestyle='-', label='Promedio por mes')
axs[0].axhline(media, color='green', linestyle='--', label=f'Media = {media:.2f}')
axs[0].axhline(UCL_x, color='red', linestyle='--', label=f'UCL = {UCL_x:.2f}')
axs[0].axhline(LCL_x, color='red', linestyle='--', label=f'LCL = {LCL_x:.2f}')
axs[0].set_title('Gráfico de Control X-barra')
axs[0].set_ylabel('Características')
axs[0].legend()
axs[0].grid(True)
axs[0].tick_params(axis='x', rotation=45)

# Gráfico R
axs[1].plot(df['Mes'], df['Rango'], marker='o', linestyle='-', color='orange', label='Rango por mes')
axs[1].axhline(media_r, color='green', linestyle='--', label=f'Media R = {media_r:.2f}')
axs[1].axhline(UCL_r, color='red', linestyle='--', label=f'UCL R = {UCL_r:.2f}')
axs[1].axhline(LCL_r, color='red', linestyle='--', label=f'LCL R = {LCL_r:.2f}')
axs[1].set_title('Gráfico de Control R')
axs[1].set_ylabel('Rango')
axs[1].legend()
axs[1].grid(True)
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
