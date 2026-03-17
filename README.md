# analisis-costos-AxI-powerbi
Proyecto End-to-End de Data Engineering y BI automatizando el Ajuste por Inflación contable.

# 📊 Data Engineering & BI: Automatización del Ajuste por Inflación (AxI)

## 🎯 Objetivo del Proyecto
En un contexto de alta inflación, el análisis de costos basado en valores históricos genera una "ilusión monetaria" que distorsiona los márgenes de rentabilidad y descapitaliza a las empresas. 

Este proyecto es una solución **End-to-End** que automatiza el cálculo del Ajuste por Inflación (basado en la RT 6) sobre una estructura de costos. A través de un pipeline de datos, se extraen índices oficiales, se transforman en una base relacional y se visualiza el impacto financiero real en un dashboard gerencial.

<img width="1012" height="579" alt="costos" src="https://github.com/user-attachments/assets/6c9b7f42-1ca2-4fbb-aceb-1838b9904fd0" />

## 🛠️ Stack Tecnológico
* **Python (Pandas):** Data Wrangling, limpieza de archivos gubernamentales complejos y Data Mocking.
* **MySQL:** Modelado de datos (Data Warehouse), sentencias DDL/DML y creación de Vistas para cálculos dinámicos.
* **Power BI & DAX:** Visualización de datos, formato condicional y creación de métricas financieras.

## ⚙️ Arquitectura y Proceso (Pipeline)

### 1. Extracción y Transformación (Python)
* **Limpieza de Datos del INDEC:** Se desarrolló un script para procesar el archivo oficial de Índices de Precios al Consumidor (IPC). El código resuelve problemas de formato mixto, filas vacías (NaN) y formatos numéricos incompatibles, exportando una tabla de dimensión limpia (`dim_indices_inflacion.csv`).
* **Data Mocking:** Se generó un dataset simulado de 500 transacciones históricas (`fact_gastos_historicos.csv`) con valores nominales que reflejan el comportamiento de precios en Argentina entre 2020 y 2026.

### 2. Modelado y Motor de Cálculo (MySQL)
Se diseñó un modelo relacional de estrella (Star Schema) y se desarrolló la vista lógica `vw_gastos_ajustados_axi`. 
Esta vista realiza un cruce dinámico que:
* Asigna a cada transacción el índice de inflación de su mes de origen.
* Identifica automáticamente el último índice disponible (mes de cierre).
* Calcula el **Coeficiente de Reexpresión** y el nuevo valor homogéneo directamente en el motor de base de datos.

### 3. Business Intelligence (Power BI)
Se construyó un tablero gerencial enfocado en la toma de decisiones financieras:
* **Métricas DAX:** Cálculo de Gasto Nominal, Gasto Ajustado y % de Distorsión (RECPAM).
* **Análisis Visual:** Gráficos de evolución histórica que evidencian la "brecha inflacionaria" y el impacto real sobre cada categoría de costo.
* **UX/UI:** Implementación de formato condicional automático para resaltar impactos negativos en los resultados.

## 💡 Insight de Negocio
La contabilidad histórica subestima el peso real de los costos, generando márgenes de ganancia ficticios. Migrar el control de gestión a moneda homogénea permite ajustar la política de *pricing* y proteger el flujo de caja operativo frente a la licuación de los saldos monetarios.

---
*Desarrollado por Tomás - Analista de Datos*
