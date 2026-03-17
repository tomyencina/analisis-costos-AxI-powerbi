import pandas as pd

def limpiar_datos_indec():
    archivo_origen = 'sh_ipc_03_26.xls'
    
    print("⏳ Paso 1: Leyendo el archivo Excel...")
    try:
        df = pd.read_excel(archivo_origen, skiprows=5)
    except Exception as e:
        print(f"❌ Error al leer: {e}")
        return
    
    print("⏳ Paso 2: Buscando la fila EXACTA de 'Nivel general'...")
    df.rename(columns={df.columns[0]: 'Division'}, inplace=True)
    
    # LA CORRECCIÓN MÁGICA: Eliminamos espacios (strip) y buscamos coincidencia exacta
    df_general = df[df['Division'].astype(str).str.strip().str.lower() == 'nivel general'].head(1)
    
    if df_general.empty:
        print("❌ Sigue sin encontrar la fila. Revisar nombre.")
        return
        
    print("⏳ Paso 3: Aislando los valores y girando la tabla...")
    serie_indices = df_general.drop(columns=['Division']).iloc[0]
    
    df_limpio = pd.DataFrame({
        'Periodo': serie_indices.index,
        'Indice_IPC': serie_indices.values
    })
    
    print("⏳ Paso 4: Limpiando las fechas...")
    df_limpio['Periodo'] = pd.to_datetime(df_limpio['Periodo'], errors='coerce')
    df_limpio = df_limpio.dropna(subset=['Periodo'])
    
    print("⏳ Paso 5: Limpiando los índices numéricos...")
    def arreglar_numeros_indec(val):
        if isinstance(val, (int, float)): return float(val)
        val_str = str(val).strip().replace('*', '')
        if '.' in val_str and ',' in val_str:
            val_str = val_str.replace('.', '').replace(',', '.')
        elif ',' in val_str:
            val_str = val_str.replace(',', '.')
        try:
            return float(val_str)
        except:
            return None

    df_limpio['Indice_IPC'] = df_limpio['Indice_IPC'].apply(arreglar_numeros_indec)
    df_limpio = df_limpio.dropna(subset=['Indice_IPC'])
    print(f"✅ Índices numéricos que sobrevivieron: {len(df_limpio)}")
    
    print("⏳ Paso 6: Filtrando desde Enero de 2020 en adelante...")
    df_final = df_limpio[df_limpio['Periodo'] >= '2020-01-01'].copy()
    df_final = df_final.sort_values('Periodo')
    print(f"✅ Meses desde 2020: {len(df_final)}")
    
    print("⏳ Paso 7: Exportando a CSV...")
    df_final.to_csv('dim_indices_inflacion.csv', index=False)
    print(f"🎯 ¡ÉXITO TOTAL! Se generó 'dim_indices_inflacion.csv' con {len(df_final)} meses registrados.")

if __name__ == '__main__':
    limpiar_datos_indec()

    
        
        

