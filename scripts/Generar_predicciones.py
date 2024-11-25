import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
import os

# Cargar los datos
ventas_df = pd.read_csv('data/Raw/Ventas_raw.csv')

# Convertir las fechas a números para poder hacer regresión
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])
ventas_df['Fecha_numerica'] = (ventas_df['Fecha'] - ventas_df['Fecha'].min()) / np.timedelta64(1, 'D')

# Definir las variables predictoras y la variable objetivo
X = ventas_df[['Fecha_numerica']]  # Aquí puedes incluir otras características si las tienes
y = ventas_df['Cantidad']

# Dividir los datos en conjunto de entrenamiento y prueba para validación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de Deep Learning (red neuronal simple)
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_dim=1))  # Capa de entrada y primera capa oculta
model.add(layers.Dense(32, activation='relu'))  # Segunda capa oculta
model.add(layers.Dense(1))  # Capa de salida

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=0)

# Evaluar el modelo
loss = model.evaluate(X_test, y_test)
print(f'Error cuadrático medio (MSE) en conjunto de prueba: {loss:.4f}')

# Predecir ventas para el próximo año (365 días)
futuras_fechas = pd.date_range(ventas_df['Fecha'].max(), periods=366, freq='D')
futuras_fechas_numericas = (futuras_fechas - ventas_df['Fecha'].min()) / np.timedelta64(1, 'D')

# Convertir 'futuras_fechas_numericas' a un array de numpy
futuras_fechas_numericas = np.array(futuras_fechas_numericas)

# Realizar la predicción para el próximo año
predicciones = model.predict(futuras_fechas_numericas.reshape(-1, 1))

# Crear la carpeta "Predicciones" dentro de "Reports" si no existe
os.makedirs('Reports/Predicciones', exist_ok=True)

# Graficar las predicciones y compararlas con los datos reales
plt.figure(figsize=(10, 6))
plt.plot(ventas_df['Fecha'], ventas_df['Cantidad'], label='Ventas Reales', color='blue')
plt.plot(futuras_fechas, predicciones, label='Predicción para el Próximo Año', linestyle='--', color='red')
plt.title('Predicción de Ventas para el Próximo Año')
plt.xlabel('Fecha')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Reports/Predicciones/predicciones_ventas_proximo_ano.png')

# Graficar la pérdida de entrenamiento
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Pérdida en Entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida en Validación')
plt.title('Pérdida durante el Entrenamiento')
plt.xlabel('Épocas')
plt.ylabel('Pérdida (MSE)')
plt.legend()
plt.tight_layout()
plt.savefig('Reports/Predicciones/perdida_entrenamiento.png')

# Graficar Predicción vs Valor Real en el conjunto de prueba
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, label='Valor Real', color='blue')
plt.scatter(X_test, model.predict(X_test), label='Predicción', color='red')
plt.title('Predicción vs Valor Real')
plt.xlabel('Fecha Numérica')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.tight_layout()
plt.savefig('Reports/Predicciones/prediccion_vs_real.png')

# Graficar la evolución de las predicciones
plt.figure(figsize=(10, 6))
plt.plot(futuras_fechas, predicciones, label='Predicción para el Próximo Año', linestyle='--', color='red')
plt.title('Evolución de la Predicción para el Próximo Año')
plt.xlabel('Fecha')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Reports/Predicciones/evolucion_prediccion.png')

print("Predicciones y gráficas generadas con éxito.")
