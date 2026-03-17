import pandas as pd
import random
from datetime import datetime, timedelta

def generar_fact_gastos():
    print("⏳ Paso 1: Iniciando el motor de Data Mocking...")
    
    # Parámetros básicos
    fecha_inicio = datetime(2020, 1, 1)
    fecha_fin = datetime(2026, 2, 28)
    cantidad_registros = 500 # Vamos a generar 500 facturas/gastos
    
    # Categorías contables típicas
    categorias = [
        'Bienes de Uso - Maquinaria',
        'Bienes de Uso - Equipos de Computacion',
        'Mercaderia de Reventa',
        'Gastos Administrativos - Alquiler',
        'Gastos Administrativos - Honorarios',
        'Gastos Comerciales - Publicidad'
    ]
    
    datos = []
    
    print("⏳ Paso 2: Generando transacciones históricas...")
    for i in range(cantidad_registros):
        # 1. Generar una fecha aleatoria entre 2020 y 2026
        dias_totales = (fecha_fin - fecha_inicio).days
        dias_random = random.randint(0, dias_totales)
        fecha_gasto = fecha_inicio + timedelta(days=dias_random)
        
        # 2. Elegir categoría aleatoria
        categoria = random.choice(categorias)
        
        # 3. Simular un monto base según la categoría
        if 'Maquinaria' in categoria:
            monto_base = random.randint(100000, 500000)
        elif 'Computacion' in categoria:
            monto_base = random.randint(50000, 150000)
        elif 'Alquiler' in categoria:
            monto_base = random.randint(30000, 80000)
        else:
            monto_base = random.randint(5000, 40000)
            
        # 4. Factor inflacionario nominal (para que los montos sean mayores en años recientes)
        # Esto hace que el dataset parezca de una empresa argentina real
        anio = fecha_gasto.year
        multiplicador = 1
        if anio == 2021: multiplicador = 1.5
        elif anio == 2022: multiplicador = 2.5
        elif anio == 2023: multiplicador = 6.0
        elif anio == 2024: multiplicador = 15.0
        elif anio >= 2025: multiplicador = 25.0
        
        monto_historico = round(monto_base * multiplicador, 2)
        
        # Guardamos la fila
        datos.append({
            'ID_Transaccion': f"TRX-{1000 + i}",
            'Fecha_Origen': fecha_gasto.strftime('%Y-%m-%d'),
            'Categoria_Gasto': categoria,
            'Importe_Historico': monto_historico
        })
        
    print(f"✅ Se generaron {len(datos)} transacciones.")
    
    print("⏳ Paso 3: Armando la estructura y exportando...")
    df_gastos = pd.DataFrame(datos)
    
    # Ordenamos cronológicamente para que quede prolijo
    df_gastos = df_gastos.sort_values('Fecha_Origen')
    
    # Exportamos a CSV
    nombre_archivo = 'fact_gastos_historicos.csv'
    df_gastos.to_csv(nombre_archivo, index=False)
    
    print(f"🎯 ¡ÉXITO TOTAL! Archivo '{nombre_archivo}' listo para usar en MySQL.")

if __name__ == '__main__':
    generar_fact_gastos()