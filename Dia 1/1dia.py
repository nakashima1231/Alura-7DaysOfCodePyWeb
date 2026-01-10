import requests

r = requests.get("https://last-airbender-api.fly.dev/api/v1/characters")
arquivo = r.json()


print(arquivo)

#correcao da alura

#import json
#import requests

#def personagens():

#   api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

#    response = requests.get(api_url)

#    print(json.dumps(response.json(), indent=4))

#personagens()
