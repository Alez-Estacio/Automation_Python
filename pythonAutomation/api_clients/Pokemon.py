import requests

def pokemon_byName_GET(pokemonName: str):
    url: str = "https://pokeapi.co/"
    fullurl: str = url + "api/v2/pokemon/" + pokemonName
    response = requests.get(fullurl)
    return response


def pokemon_byNumber_GET(pokemonNumber: int):
    url: str = "https://pokeapi.co/"
    fullurl: str = url + "api/v2/pokemon/" + str(pokemonNumber)
    response = requests.get(fullurl)
    return response

