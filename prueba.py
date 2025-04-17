# Importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Creamos algunos datos de ejemplo
fechas = pd.date_range(start='2024-01-01', periods=10, freq='D')
temperaturas = np.random.randint(15, 35, size=10)
humedad = np.random.randint(40, 90, size=10)

# Creamos un DataFrame con estos datos
datos = pd.DataFrame({
    'fecha': fechas,
    'temperatura': temperaturas,
    'humedad': humedad
})

# Mostramos los primeros registros
print("Datos generados:")
print(datos.head())

# Hacemos un análisis básico
print("\nEstadísticas descriptivas:")
print(datos.describe())

print(f"\nTemperatura media: {datos['temperatura'].mean():.2f}°C")
print(f"Día más caluroso: {datos.loc[datos['temperatura'].idxmax(), 'fecha'].strftime('%Y-%m-%d')}")

# Creamos una visualización
plt.figure(figsize=(10, 6))
plt.plot(datos['fecha'], datos['temperatura'], 'r-o', label='Temperatura (°C)')
plt.plot(datos['fecha'], datos['humedad'], 'b-o', label='Humedad (%)')
plt.title('Registro de temperatura y humedad')
plt.xlabel('Fecha')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Guardamos el gráfico en un archivo
plt.savefig('clima_grafico.png')

# También mostramos el gráfico si estamos en un entorno interactivo
plt.show()

print("\nAnálisis completado. Se ha guardado el gráfico como 'clima_grafico.png'")