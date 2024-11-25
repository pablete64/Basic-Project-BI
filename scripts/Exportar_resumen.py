import pandas as pd

# Cargar el archivo CSV
ventas_df = pd.read_csv('data/Raw/Ventas_raw.csv')

# Resumen de ventas totales por producto
resumen = ventas_df.groupby('Producto').agg(
    Total_Ventas=('Cantidad', 'sum'),
    Total_Valor=('Precio', 'sum')
).reset_index()

# Exportar el resumen a un archivo CSV
resumen.to_csv('Reports/Resumen_ventas.csv', index=False)

# O también podrías exportar como un archivo de texto:
with open('Reports/Resumen_ventas.txt', 'w') as f:
    f.write(resumen.to_string(index=False))

print("Resumen de ventas exportado con éxito.")
