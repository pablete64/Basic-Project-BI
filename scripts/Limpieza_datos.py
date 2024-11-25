import pandas as pd

# Cargar los datos
ventas_df = pd.read_csv('data/Raw/Ventas_raw.csv')

# Eliminar filas con valores nulos
ventas_df = ventas_df.dropna()

# Eliminar registros duplicados
ventas_df = ventas_df.drop_duplicates()

# Asegurarse de que las fechas sean del tipo datetime
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])

# Guardar los datos limpios
ventas_df.to_csv('data/Processed/Ventas_limpias.csv', index=False)

print("Datos limpiados y exportados con éxito.")
