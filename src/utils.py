import requests
import json
import pandas as pd


# Retorna erros e paraliza o programa corretamente, imprimindo x
def error(x):
    raise ValueError(x)


# Concatena e retorna a url do API com o endpoint desejado
def url_join(endpoint):
    api_url = 'https://api.intra.42.fr/v2'
    url = api_url + endpoint
    return url


# Converte bytes para dictionary, utilizando json
def bytetodict(response):
    res_dict = json.loads(response.decode('utf-8'))
    return res_dict


# Analisa se recebeu user_id ou login, retornando o id correto para uso do API
# Em caso de recebimento de login, faz busca em 100 páginas pelo login
def get_user_id(arg, headers):
    if arg.isnumeric() is True:
        user_id = arg
    else:
        login = arg
        endpoint = '/users/%s' % login
        url = url_join(endpoint)
        response = requests.get(url, headers=headers)
        uid = bytetodict(response.content)
        if uid == {}:
            return None
        user_id = uid['login']
    return user_id

	
# Imprime o DataFrame de acordo com a flag recebida
# Trata listas caso a flag precise imprimir e também manuseia uma exceção
def print_infos(df, flag):
    if (flag is None):
        print(df)
    else:
        if (flag == 'staff'):
            flag = 'staff?'
        if df.index.str.contains(flag).any():
            if df[flag] == []:
                error('This section is empty')
            if (isinstance(df[flag], list)):
                df = pd.Series(df[flag])
                df = pd.Series(df[0])
                pd.set_option('display.max_colwidth', None)
                with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
                    print(df)
            else:
                print(df[flag])
        else:
            error('Flag not found')
