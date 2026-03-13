from analisis import (cargar_y_limpiar_datos, mostrar_promedio_cs,
                      mostrar_winrate_campeon, graficar_campeones_jugados,
                      graficar_top_kills, mostrar_top_kda, mostrar_correlacion)


def iniciar_programa():
    print("Cargando base de datos y limpiando formatos...")
    df = cargar_y_limpiar_datos()

    if df is None:
        return  # Si no encuentra el Excel, corta el programa acá

    print("¡Datos listos y cargados con éxito!")

    while True:
        print("\n" + "=" * 45)
        print("📊 MENÚ DE ANÁLISIS DE RENDIMIENTO - LOL")
        print("=" * 45)
        print("1. Ver promedio de CS/min (Global y por Rol)")
        print("2. Ver Winrate % por Campeón")
        print("3. Gráfico: Campeones más jugados")
        print("4. Gráfico: Promedio de Kills por Campeón")
        print("5. Ver Top 5 partidas por KDA")
        print("6. Bonus: Matriz de Correlación de Victorias")
        print("0. Salir")

        opcion = input("\nIngresá el número de la opción: ")

        if opcion == '1':
            mostrar_promedio_cs(df)
        elif opcion == '2':
            mostrar_winrate_campeon(df)
        elif opcion == '3':
            graficar_campeones_jugados(df)
        elif opcion == '4':
            graficar_top_kills(df)
        elif opcion == '5':
            mostrar_top_kda(df)
        elif opcion == '6':
            mostrar_correlacion(df)
        elif opcion == '0':
            print("\nCerrando terminal... ¡GG WP!")
            break
        else:
            print("\n[Error] Comando no reconocido. Ingresá un número del 0 al 6.")


# Punto de entrada de Python
if __name__ == "__main__":
    iniciar_programa()