from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="viaje_chile_peru")

print("===================================")
print("  DISTANCIA CHILE - PERÚ")
print("===================================")

while True:

    origen = input("\nCiudad de Origen (Chile) o 's' para salir: ")

    if origen.lower() == "s":
        print("Programa finalizado.")
        break

    destino = input("Ciudad de Destino (Perú): ")

    if destino.lower() == "s":
        print("Programa finalizado.")
        break

    transporte = input(
        "\nMedio de transporte (auto, bus, avion): "
    ).lower()

    try:

        ciudad_origen = geolocator.geocode(origen + ", Chile")
        ciudad_destino = geolocator.geocode(destino + ", Peru")

        if ciudad_origen is None or ciudad_destino is None:
            print("\nNo fue posible encontrar alguna de las ciudades.")
            continue

        distancia = geodesic(
            (ciudad_origen.latitude, ciudad_origen.longitude),
            (ciudad_destino.latitude, ciudad_destino.longitude)
        )

        kilometros = distancia.kilometers
        millas = distancia.miles

        if transporte == "auto":
            velocidad = 80

        elif transporte == "bus":
            velocidad = 70

        elif transporte == "avion":
            velocidad = 800

        else:
            print("\nMedio de transporte no válido.")
            continue

        horas = kilometros / velocidad

        print("\n========== RESULTADO ==========")
        print(f"Ciudad Origen : {origen}")
        print(f"Ciudad Destino: {destino}")
        print(f"Distancia     : {kilometros:.2f} km")
        print(f"Distancia     : {millas:.2f} millas")
        print(f"Duración      : {horas:.2f} horas")
        print("\nNarrativa del viaje:")
        print(
            f"Viajarás desde {origen}, Chile, hasta {destino}, Perú "
            f"utilizando {transporte}. "
            f"Recorrerás aproximadamente {kilometros:.2f} kilómetros "
            f"({millas:.2f} millas) y el viaje tendrá una duración "
            f"estimada de {horas:.2f} horas."
        )

    except Exception as e:
        print("Error:", e)
