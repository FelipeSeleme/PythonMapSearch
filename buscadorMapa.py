import folium
from geopy.geocoders import Nominatim
import webbrowser
import os

# Entrada do usuário
lugar_nome = input("Insira o lugar: ")

# Inicializa o geolocalizador
geolocator = Nominatim(user_agent="buscadorMapa")
local = geolocator.geocode(lugar_nome)

if local:
    # Obtém coordenadas
    latitude, longitude = local.latitude, local.longitude
    
    # Cria o mapa
    mapa = folium.Map(location=[latitude, longitude], zoom_start=15)
    
    # Adiciona um marcador
    folium.Marker([latitude, longitude], popup=lugar_nome).add_to(mapa)
    
    # Salva o mapa como HTML
    mapa_path = os.path.abspath("mapa.html")  # Caminho absoluto do arquivo
    mapa.save(mapa_path)
    
    # Abre o navegador automaticamente
    webbrowser.open("file://" + mapa_path)

    print("Mapa salvo como 'mapa.html' e aberto no navegador.")

else:
    print("Local não encontrado. Tente novamente.")
