import pandas as pd
from scipy.stats import binomtest

# 1. Cargar los datos
# Cambiá 'partidas.xlsx' por el nombre real de tu archivo
print("Cargando base de datos...")
df = pd.read_excel('datos_lol.xlsx')

# A. Convertir la columna 'victoria' a valores booleanos (1 y 0)
# Usamos .map() que es súper eficiente para reemplazar valores exactos
df['victoria'] = df['victoria'].map({'si': 1, 'no': 0})

# B. Convertir 'duracion_min' (ej: "29:52") a un número decimal (ej: 29.86)
# Primero nos aseguramos de que sea texto (string) por si Excel lo guardó raro
df['duracion_min_str'] = df['duracion_min'].astype(str)

# Separamos los minutos de los segundos usando los dos puntos ":"
tiempo_separado = df['duracion_min_str'].str.split(':', expand=True)

# Convertimos los pedazos a números y calculamos el decimal
minutos = tiempo_separado[0].astype(float)
segundos = tiempo_separado[1].astype(float)

# Sobreescribimos la columna original con el valor matemático real
df['duracion_min'] = minutos + (segundos / 60)



# 3. Mostrar el resultado para verificar
'''print("\n--- Primeras 5 filas con los datos limpios ---")
print(df[['fecha_hora', 'duracion_min', 'campeon', 'rol', 'kills', 'deaths', 'assists', 'cs', 'vision_score', 'victoria', 'duracion_min_str']])

print("\n--- Lista de Columnas ---")
print(df.columns.tolist())

#crear una nueva columna con el cs por minuto de cada match'''
df['cs_por_minuto'] = df['cs'] / df['duracion_min']
'''print(df[['duracion_min', 'cs',  'cs_por_minuto']].head(5))'''

#calcular el promedio general de cs por minuto
promedio_cs_por_minuto = df['cs_por_minuto'].mean()
'''print("el promedio de cs por minuto es de: ", round(promedio_cs_por_minuto, 2))'''

#calcular el promedio por campeon de cs por minuto
cs_por_campeon = df.groupby('campeon')['cs'].mean()
print("el cs por campeon es de: ", round(cs_por_campeon, 2))

#tengo un 90% de probabilidades de ganar con un cs mayor a 200 con significancia del 0,01
match_mas_200_cs = df[df['cs']>=200]
cantidad_match_mas_200_cs_ganados = match_mas_200_cs[match_mas_200_cs['victoria']==1]
print(len(cantidad_match_mas_200_cs_ganados))

resultados = binomtest(len(cantidad_match_mas_200_cs_ganados), len(match_mas_200_cs), p=0.7, alternative='two-sided')
print(resultados)




