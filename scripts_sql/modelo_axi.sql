CREATE DATABASE IF NOT EXISTS db_analisis_costos;
USE db_analisis_costos;


CREATE TABLE dim_indices_inflacion (
    Periodo DATE PRIMARY KEY,
    Indice_IPC DECIMAL(15, 4) 


CREATE TABLE fact_gastos_historicos (
    ID_Transaccion VARCHAR(20) PRIMARY KEY,
    Fecha_Origen DATE,
    Categoria_Gasto VARCHAR(100),
    Importe_Historico DECIMAL(15, 2)
);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dim_indices_inflacion.csv'
INTO TABLE dim_indices_inflacion
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS
(Periodo, Indice_IPC);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/fact_gastos_historicos.csv'
INTO TABLE fact_gastos_historicos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS
(ID_Transaccion, Fecha_Origen, Categoria_Gasto, Importe_Historico);


CREATE OR REPLACE VIEW vw_gastos_ajustados_axi AS
SELECT 
    g.ID_Transaccion,
    g.Fecha_Origen,
    g.Categoria_Gasto,
    g.Importe_Historico,
    i_origen.Periodo AS Mes_Origen,
    i_origen.Indice_IPC AS Indice_Origen,
    i_cierre.Indice_IPC AS Indice_Cierre,
    ROUND(i_cierre.Indice_IPC / i_origen.Indice_IPC, 4) AS Coeficiente_AxI,
    ROUND(g.Importe_Historico * (i_cierre.Indice_IPC / i_origen.Indice_IPC), 2) AS Importe_Ajustado
FROM 
    fact_gastos_historicos g
LEFT JOIN 
    dim_indices_inflacion i_origen 
    ON DATE_FORMAT(g.Fecha_Origen, '%Y-%m-01') = i_origen.Periodo
CROSS JOIN 
    (SELECT Indice_IPC FROM dim_indices_inflacion ORDER BY Periodo DESC LIMIT 1) AS i_cierre;


SELECT * FROM vw_gastos_ajustados_axi LIMIT 10;