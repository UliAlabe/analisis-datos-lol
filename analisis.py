import pandas as pd

def cargar_y_limpiar_datos():
    """Carga el Excel y prepara las columnas matemáticas."""
    try:
        df = pd.read_excel('datos_lol.xlsx')
    except FileNotFoundError:
        print("\n[Error] No se encontró el archivo 'partidas.xlsx'.")
        return None

    #Solucion para espacios en blanco con campeones
    df['campeon'] = df['campeon'].str.strip()

    # Transformación de datos
    df['victoria'] = df['victoria'].map({'si': 1, 'no': 0})

    tiempo_separado = df['duracion_min'].astype(str).str.split(':', expand=True)
    df['duracion_min'] = tiempo_separado[0].astype(float) + (tiempo_separado[1].astype(float) / 60)
    df['cs_por_minuto'] = df['cs'] / df['duracion_min']

    # Ingeniería de KDA (evitando división por cero)
    df['kda'] = (df['kills'] + df['assists']) / df['deaths'].replace(0, 1)

    return df
# --- OPCIÓN 1 ---
def mostrar_promedio_cs(df):
    print("\n--- El promedio de cs global --- \n", (df['cs_por_minuto'].mean().round(2)))
    promedio_cs_rol = (df.groupby('rol')['cs_por_minuto'].mean()).round(2)
    print("\n--- El promedio de cs por rol es ---\n", promedio_cs_rol.to_string())

# --- OPCIÓN 2 ---
def mostrar_winrate_campeon(df):
    print("\n--- Winrate % por Campeón ---")
    # Agrupamos por campeón, sacamos el promedio de victorias y pasamos a %
    winrate = df.groupby('campeon')['victoria'].mean() * 100
    print(winrate.round(2).sort_values(ascending=False).to_string())

# --- OPCIONES 3 y 4 (Gráficos pendientes) ---
def graficar_campeones_jugados(df):
    print("\n--- Campeones más jugados ---")
    print(df['campeon'].value_counts().head(5).to_string())
    print("\n[!] En construcción: Falta integrar Matplotlib para el gráfico de barras.")
    # Acá irá el df['campeon'].value_counts()

def graficar_top_kills(df):
    print("\n--- kills por campeon ---")
    print(df.groupby('campeon')['kills'].mean().round(2).to_string())
    print("\n[!] En construcción: Falta integrar Matplotlib para el gráfico de kills.")

# --- OPCIÓN 5 ---
def mostrar_top_kda(df):
    print("\n--- Top 5 Partidas por KDA ---")
    top_5 = df.sort_values(by='kda', ascending=False).head(5)
    print(top_5[['campeon', 'rol', 'kills', 'deaths', 'assists', 'kda']].round(2))

# --- OPCIÓN 6 (Bonus) ---
def mostrar_correlacion(df):
    print("\n[!] En construcción: Analizador matemático de variables.")



