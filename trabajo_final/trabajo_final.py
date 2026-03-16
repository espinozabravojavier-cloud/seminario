import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Paso 1: Creación del Dataset
datos = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E', 
                 'Producto F', 'Producto G', 'Producto H', 'Producto I', 'Producto J'],
    'Precio': [100, 150, 200, 250, 300, 120, 180, 130, 220, 270],
    'Cantidad': [10, 5, 8, 12, 7, 14, 6, 9, 13, 15],
    'Ciudad': ['Lima', 'Arequipa', 'Cusco', 'Lima', 'Arequipa', 
               'Lima', 'Arequipa', 'Cusco', 'Lima', 'Arequipa']
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("DataFrame Original:")
print(df)

# Paso 2: Manipulación de Datos
# Crear la columna 'Ventas' calculada como Precio * Cantidad
df['Ventas'] = df['Precio'] * df['Cantidad']

# Mostrar el DataFrame actualizado
print("\nDataFrame con la columna 'Ventas':")
print(df)

# Paso 3: Calcular estadísticas
promedio_ventas = df['Ventas'].mean()
venta_maxima = df['Ventas'].max()
venta_minima = df['Ventas'].min()
suma_total_ventas = df['Ventas'].sum()

print(f"\nPromedio de ventas: {promedio_ventas}")
print(f"Venta máxima: {venta_maxima}")
print(f"Venta mínima: {venta_minima}")
print(f"Suma total de ventas: {suma_total_ventas}")

# Paso 4: Filtrado de Datos
# Filtrar ventas realizadas en Lima
ventas_lima = df[df['Ciudad'] == 'Lima']
# Filtrar productos con ventas mayores a 1000
ventas_mayores_1000 = df[df['Ventas'] > 1000]
# Filtrar productos con cantidad vendida mayor a 5
cantidad_mayor_5 = df[df['Cantidad'] > 5]

print(f"\nVentas en Lima:\n{ventas_lima}")
print(f"\nVentas mayores a 1000:\n{ventas_mayores_1000}")
print(f"\nProductos con cantidad mayor a 5:\n{cantidad_mayor_5}")

# Paso 5: Cálculos con NumPy
# Convertir la columna 'Ventas' a un array de NumPy
ventas_array = np.array(df['Ventas'])

# Calcular estadísticas con NumPy
media_ventas = np.mean(ventas_array)
desviacion_estandar = np.std(ventas_array)
maximo_ventas = np.max(ventas_array)
minimo_ventas = np.min(ventas_array)

print(f"\nMedia de ventas: {media_ventas}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Valor máximo de ventas: {maximo_ventas}")
print(f"Valor mínimo de ventas: {minimo_ventas}")

# Paso 6: Visualización de Datos
# 1. Gráfico de barras (Ventas por producto)
plt.figure(figsize=(10, 6))
plt.bar(df['Producto'], df['Ventas'], color='skyblue')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.title('Ventas por Producto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Gráfico de línea (Cantidad vendida por producto)
plt.figure(figsize=(10, 6))
plt.plot(df['Producto'], df['Cantidad'], marker='o', color='green')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.title('Cantidad Vendida por Producto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Gráfico de pastel (Distribución de ventas por ciudad)
ciudad_ventas = df.groupby('Ciudad')['Ventas'].sum()
plt.figure(figsize=(8, 8))
plt.pie(ciudad_ventas, labels=ciudad_ventas.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Ventas por Ciudad')
plt.show()

# Paso 7: Responder a las Preguntas
producto_mayor_venta = df.loc[df['Ventas'].idxmax()]['Producto']
ciudad_mayor_volumen_ventas = df.groupby('Ciudad')['Ventas'].sum().idxmax()

print(f"\nProducto que genera mayores ventas: {producto_mayor_venta}")
print(f"Ciudad con mayor volumen de ventas: {ciudad_mayor_volumen_ventas}")
print(f"Promedio de ventas: {promedio_ventas}")
print(f"¿Existe mucha variación en las ventas? {'Sí' if desviacion_estandar > 100 else 'No'}")

# Paso 8: Generar un Dataset Más Grande
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E', 'Producto F', 'Producto G', 'Producto H', 'Producto I', 'Producto J']
ciudades = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Chiclayo']
regiones = ['Región 1', 'Región 2', 'Región 3', 'Región 4', 'Región 5', 'Región 6', 'Región 7', 'Región 8', 'Región 9', 'Región 10', 'Región 11', 'Región 12', 'Región 13', 'Región 14', 'Región 15']

# Generar datos aleatorios
datos_grandes = {
    'Producto': [random.choice(productos) for _ in range(300)],
    'Precio': [random.randint(100, 300) for _ in range(300)],
    'Cantidad': [random.randint(1, 20) for _ in range(300)],
    'Ciudad': [random.choice(ciudades) for _ in range(300)],
    'Región': [random.choice(regiones) for _ in range(300)]
}

df_grande = pd.DataFrame(datos_grandes)

# Mostrar una parte del DataFrame para comprobar
print(f"\nPrimeras filas del nuevo Dataset:\n{df_grande.head()}")

# Paso 9: Graficar
# 1. Histograma de ventas
plt.figure(figsize=(10, 6))
plt.hist(df_grande['Precio'] * df_grande['Cantidad'], bins=20, color='orange', edgecolor='black')
plt.title('Histograma de Ventas')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.show()

# 2. Gráfico de dispersión (Precio vs Cantidad)
plt.figure(figsize=(10, 6))
plt.scatter(df_grande['Precio'], df_grande['Cantidad'], color='purple')
plt.title('Precio vs Cantidad Vendida')
plt.xlabel('Precio')
plt.ylabel('Cantidad Vendida')
plt.show()