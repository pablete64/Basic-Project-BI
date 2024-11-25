import os
import subprocess

# Verificar que las carpetas necesarias existan
os.makedirs('Reports/Visuals', exist_ok=True)

# Ejecutar los scripts
subprocess.run(['python', 'Scripts/Limpieza_datos.py'])
subprocess.run(['python', 'Scripts/Exportar_resumen.py'])
subprocess.run(['python', 'Scripts/Generar_graficos.py'])
subprocess.run(['python', 'Scripts/Generar_predicciones.py'])

print("Análisis completo.")
