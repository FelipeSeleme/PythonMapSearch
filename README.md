# 🌍 Mapa Interativo com Folium

Este projeto gera um mapa interativo baseado em um local informado pelo usuário. O código utiliza **Python**, as bibliotecas **Folium** e **Geopy** para geocodificação, e **Webbrowser** para abrir automaticamente o mapa no navegador.

## Funcionalidades
- O usuário insere um nome de local.
- O código obtém as coordenadas geográficas desse local.
- Um mapa interativo é gerado e salvo como um arquivo `mapa.html`.
- O mapa é aberto automaticamente no navegador.

## Dependências
Antes de rodar o código, instale as dependências necessárias:
```bash
pip install folium geopy
```

## Como Usar
1. **Execute o script Python**
```bash
python mbuscadorMapa.py
```
2. **Digite o nome de um local** (exemplo: "Florianópolis").
3. **O mapa será salvo e aberto automaticamente no navegador**.


## Notas
- Certifique-se de estar conectado à internet, pois o `Nominatim` precisa acessar um serviço online para geocodificação.
- O código é compatível com **Windows, macOS e Linux**.
- Pode ser rodado tanto em **Jupyter Notebook** quanto em um script Python normal.

## Licença
Este projeto é de código aberto e pode ser modificado conforme necessário.