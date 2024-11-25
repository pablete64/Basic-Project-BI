import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
ventas_df = pd.read_csv('data/Raw/Ventas_raw.csv')

# Graficar las ventas totales por producto
ventas_por_producto = ventas_df.groupby('Producto').agg(Total_Ventas=('Cantidad', 'sum')).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Producto', y='Total_Ventas', data=ventas_por_producto)
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Reports/Visuals/ventas_por_producto.png')
plt.clf()

# Graficar las ventas por región
ventas_por_region = ventas_df.groupby('Región').agg(Total_Ventas=('Cantidad', 'sum')).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Región', y='Total_Ventas', data=ventas_por_region)
plt.title('Ventas Totales por Región')
plt.xlabel('Región')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Reports/Visuals/ventas_por_region.png')

print("Gráficos generados con éxito.")
