#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[45]:


df = pd.read_excel("data.xlsx")
print(df.shape)


# In[46]:


# Identificar las filas duplicadas
duplicados = df[df.duplicated(keep=False)]
print(duplicados)


# In[47]:


# Obtener los IDs de las filas duplicadas
ids_duplicados = duplicados['ID'].values.tolist()
print(ids_duplicados)


# In[48]:


df = df.drop_duplicates()
print(df.shape)


# In[49]:


# Obtener el número total de elementos faltantes
num_faltantes = df.isnull().sum().sum()

# Obtener el número total de elementos
num_total = df.count().sum()

# Porcnetaje de datos faltantes

percent = round(num_faltantes*100.0 / num_total, 2)

print("Número total de elementos faltantes:", num_faltantes)
print("Número total de elementos:", num_total)
print("Porcentaje de datos faltantes:", percent)


# In[50]:


print(df)


# In[51]:


# Eliminar filas que contienen datos vacíos en la columna 'Columna'
df = df.dropna(subset=['quality'])

# Restablecer los índices del dataframe resultante
df = df.reset_index(drop=True)


# In[54]:


df = df.dropna(axis=1)


# In[55]:


print(df)


# In[57]:


df.to_excel("data_1.xlsx")


# In[61]:


conteo_2000 = df[(df['cosecha'] == 2000) & (df['quality'] == 'A')].shape[0]

# Contar vinos de la cosecha 2022 con calidad 'A'
conteo_2022 = df[(df['cosecha'] == 2022) & (df['quality'] == 'A')].shape[0]

# Mostrar los resultados
print("Cantidad de vinos de la cosecha 2000 con calidad 'A':", conteo_2000)
print("Cantidad de vinos de la cosecha 2022 con calidad 'A':", conteo_2023)


# In[65]:


# Crear un diagrama de cajas utilizando Seaborn
sns.boxplot(x='pH', y='density', data=df)

# Calcular los límites superior e inferior
q1 = df.groupby('pH')['density'].quantile(0.25)
q3 = df.groupby('pH')['density'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Mostrar los límites superior e inferior
print("Límite inferior:")
print(limite_inferior)
print("Límite superior:")
print(limite_superior)



# In[69]:


# Método de los cuartiles
q1 = df['free sulfur dioxide'].quantile(0.25)
q3 = df['free sulfur dioxide'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Identificar valores atípicos utilizando el método de los cuartiles
valores_atipicos_cuartiles = df[(df['free sulfur dioxide'] < limite_inferior) | (df['free sulfur dioxide'] > limite_superior)]

# Método de la desviación estándar
media = df['free sulfur dioxide'].mean()
desviacion_estandar = df['free sulfur dioxide'].std()
limite_inferior_std = media - 2 * desviacion_estandar
limite_superior_std = media + 2 * desviacion_estandar

# Identificar valores atípicos utilizando el método de la desviación estándar
valores_atipicos_std = df[(df['free sulfur dioxide'] < limite_inferior_std) | (df['free sulfur dioxide'] > limite_superior_std)]

# Limpiar los datos atípicos utilizando el método de los cuartiles
df_limpio_cuartiles = df[(df['free sulfur dioxide'] >= limite_inferior) & (df['free sulfur dioxide'] <= limite_superior)]

# Limpiar los datos atípicos utilizando el método de la desviación estándar
df_limpio_std = df[(df['free sulfur dioxide'] >= limite_inferior_std) & (df['free sulfur dioxide'] <= limite_superior_std)]

# Comparar los resultados
print("Valores atípicos (método de los cuartiles):")
print(valores_atipicos_cuartiles)
print()
print("Valores atípicos (método de la desviación estándar):")
print(valores_atipicos_std)
print()
print("Data limpia (método de los cuartiles):")
print(df_limpio_cuartiles)
print()
print("Data limpia (método de la desviación estándar):")
print(df_limpio_std)


# In[ ]:




