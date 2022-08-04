# Student search
O intuito da aplicação é fazer buscas por informações de um dado usuário.
A aplicação requere os dados pelo API (https://api.intra.42.fr) e imprime em forma de tabela.
Para especificação de dados, ou filtro dos mesmos, usar flags.

## Utilitários
O programa foi desenvolvido em Python, usando pandas, JSON e requests, estes devem ser instalados.

- Comando de instalação para o Mac: JSON está incluso na biblioteca padrão do Python. Dependendo da versão do Python, talvez o comando "pip" deva ser substituido por "pip3"
`pip install pandas`
`pip install requests`

- Verificação de funcionalidade: No arquivo student-search.py, a primeira linha de código (`#!/usr/bin/python3`) dever ser compatível com o local em que se encontra a versão do Python a ser utilizada

- Sempre que houver algum erro na entrada de informações, o programa retornará o mesmo com **ValueError**

- Norma do código: Todos os arquivos foram escritos seguindo norma PEP8, verificada pela ferramenta flake8. Mais informações em: https://pypi.org/project/flake8/

- Outra ferramenta útil no processo foi o conversor cURL para Python: https://curl.trillworks.com/#

## Como utilizar
Na pasta do código, basta rodar pelo terminal:

`./student-search.py "user_id" <flag>`

- **intra_id**: o intra_id é obrigatório. Este pode ser utilizado tanto pelo **número de id** como pelo **login da intra** 
- **flag**: a flag é **opcional** e apenas uma pode ser utilizada por vez.

- Flags disponíveis:
`id` `email` `login` `first_name` `last_name` `url` `phone` `displayname` `image_url` 
`staff` `correction_point` `pool_month` `pool_year` `location` `wallet` 
`anonymize_date` `cursus_users` `projects_users` `languages_users` 
`achievements` `campus` `campus_users`

- Flags parcialmente disponíveis: a maioria dos usuários não tem informações agregadas a elas, assim o programa retornará um erro.
`groups` `titles` `titles_users` `partnerships` `patroned` `patroning` `expertises_users`

## Teste
Para execução dos testes basta rodar o seguinte comando pelo terminal:

`sh tests.sh`
