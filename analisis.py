import pandas as pd
import matplotlib.pyplot as plt

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
    campeones = df['campeon'].value_counts()
    campeones.plot(kind='bar', color='salmon', edgecolor='black')
    plt.title('Campeones mas jugados', fontsize=14)
    plt.xlabel('Campeón', fontsize=12)
    plt.ylabel('cantidad', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graficar_top_kills(df):
    print("\nGenerando gráfico de Kills... revisá la barra de tareas de Windows.")

    # 1. Agrupamos por campeón, sacamos promedio de kills y ORDENAMOS de mayor a menor
    promedio_kills = df.groupby('campeon')['kills'].mean().sort_values(ascending=False)

    # 2. Le decimos a Pandas que prepare el gráfico de barras (color salmón para diferenciarlo)
    promedio_kills.plot(kind='bar', color='salmon', edgecolor='black')

    # 3. Configuramos la estética
    plt.title('Promedio de Kills por Campeón', fontsize=14)
    plt.xlabel('Campeón', fontsize=12)
    plt.ylabel('Kills Promedio', fontsize=12)

    # Rotamos etiquetas y ajustamos márgenes para que quede prolijo
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 4. Abrimos la ventana
    plt.show()
    print(promedio_kills.round(2).to_string())

# --- OPCIÓN 5 ---
def mostrar_top_kda(df):
    print("\n--- Top 5 Partidas por KDA ---")
    top_5 = df.sort_values(by='kda', ascending=False).head(5)
    print(top_5[['campeon', 'rol', 'kills', 'deaths', 'assists', 'kda']].round(2))

# --- OPCIÓN 6 (Bonus) ---
def mostrar_correlacion(df):
    print("\n--- Analizador de Impacto en la Victoria ---")
    print("¿Qué factor define realmente tus partidas?")

    # 1. Calculamos la correlación solo de las columnas numéricas
    matriz = df.corr(numeric_only=True)

    # 2. Recortamos solo la columna 'victoria'
    impacto_victoria = matriz['victoria']

    # 3. Ordenamos de mayor a menor para hacer un "Ranking de Impacto"
    ranking = impacto_victoria.sort_values(ascending=False).round(3)

    # 4. Imprimimos limpio
    print("\n", ranking.to_string())

    correlacion_farmeo_kills = df['kills'].corr(df['cs'])
    print("\nLa correlacion del fameo y la cantidad de kills es de: ", correlacion_farmeo_kills.round(2))


