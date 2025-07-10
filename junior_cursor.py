from pprint import pprint
import requests


def fazer_requisicao(url, params=None):
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro ao buscar o nome: {e}")
        resultado = None
    else: 
        resultado = response.json()

    return resultado



def frequencia_nomes_por_decada(nome):

    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    dados_decada = fazer_requisicao(url=url)
    dict_decadas = {}
    print(dados_decada)





def main(nome):
    frequencia_nomes_por_decada(nome)


if __name__ == "__main__":
    main('Maria')


