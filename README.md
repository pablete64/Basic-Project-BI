# Basic-Project-BI
This repository contains a sales data analysis project designed to process, clean, and analyze data while generating useful visualizations and predictions for decision-making. The workflow is automated through a main script that coordinates the execution of several specialized scripts, ensuring efficient data and result management.

# Clone the repository
git clone <repository_url>
cd <repository_name>

# Activate the provided virtual environment (ENTORNO)
# For Linux/Mac:
source ENTORNO/bin/activate
# For Windows:
ENTORNO\Scripts\activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the main script to execute the entire workflow
python Main.py

# Outputs:
# - Sales Summary: Reports/Resumen_ventas.csv and Reports/Resumen_ventas.txt
# - Visualizations: Reports/Visuals
# - Predictions: Reports/Predicciones

# Explanation of Scripts:
# 1. Limpieza_datos.py: Cleans raw data for analysis.
# 2. Exportar_resumen.py: Generates a summary of sales by product and exports it as CSV and text.
# 3. Generar_graficos.py: Creates visualizations of sales by product and region.
# 4. Generar_predicciones.py: Predicts future sales using a deep learning model and creates prediction graphs.
