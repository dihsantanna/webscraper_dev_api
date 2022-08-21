
# Web Scraper API

Api RESTful desenvolvida a partir de dados providos por um crawler que faz uma raspagem de dados do https://webscraper.io/test-sites/e-commerce/allinone, que é utilizado para testes de web scraping, que simula uma pequena lista de amostra de aparelhos eletrônicos.

O crawler está configurado para obter os dados de notebooks da marca lenovo e os ordena do preço mais barato para o mais caro.

## O desafio é:

* Acessar esse site https://webscraper.io/test-sites/e-commerce/allinone
* Pegar todos notebooks Lenovo ordenando do mais barato para o mais caro.
* Pegar todos os dados disponíveis dos produtos.
* É interessante que o robô possa ser consumido por outros serviços. Recomendamos a criação de uma pequena RESTFul API JSON para deixar mais otimizado.

## Stacks obrigatórias
* Utilizar `Puppeteer` ou `Playwright`.

## Stacks utilizadas

* [Python](https://www.python.org/)
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [MongoDB](https://www.mongodb.com/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
* [Playwright](https://playwright.dev/python/docs/library)
* [PyTest](https://docs.pytest.org/en/7.1.x/contents.html)

## Requisitos para instalar e rodar aplicação

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/) com o plug-in do [Docker Compose](https://docs.docker.com/compose/install/) instalado. Caso tenha alguma dificuldade sugiro procurar as respectivas documentações clicando nos links. :wink:
* Um cliente de API como [Insomnia](https://insomnia.rest/) ou [Postman](https://www.postman.com/).

*ATENÇÃO: todos os métodos de intalação e start da aplicação serão explicados utilizando o docker, por isso enfatizo a instalação dele.


## Instalação

Primeiramente baixe a aplicação. Em seu terminal insira o seguinte comando:

```bash
git clone git@github.com:dihsantanna/webscraper_dev_api.git && cd webscraper_dev_api
```

Com o docker devidamente instalado e habilitado, digite no seu terminal:

```bash
docker-compose up -d --build
```

*Este processo pode demorar alguns minutos dependendo de sua velocidade de internet.

Pronto! Sua aplicação já pode ser utilizada e a API estará rodando no http://127.0.0.1:5000/, mas o banco de dados ainda não foi populado e para fazer isso insira o comando:

```bash
docker container exec -it webscraper_api bash -c "python scrape_init.py"
```

*Esse comando serve para iniciar a raspagem de dados inicial, aguarde até o término dela.
## Usando a API

Abra o seu cliente de API. ([Insominia](https://insomnia.rest/) ou [Postman](https://www.postman.com/))

A API possui duas rotas a `/notebooks` e `/scraper`(que também pode ser utilizada com a query `orderId`),
ambas possuem método `GET`, porém só a `/scraper` possui método `POST` utilizando a query `orderId`.

### Rota GET `/notebooks`

Retorna todos os notebooks encontrados pelo scraper salvos no banco de dados, ordenados do menor para o maior preço.

O resultado é parecido com os dados abaixo:

`STATUS CODE 200`
```json
[
  {
    "_id": {
      "$oid": "63010b3c0de1e8fdcf96bc23"
    },
    "title": "Lenovo V110-15IAP",
    "description": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
    "img_src": "https://webscraper.io/images/test-sites/e-commerce/items/cart2.png",
    "price": 321.94,
    "hdd": [
      "128",
      "256",
      "512"
    ],
    "rating": {
      "qty_reviews": 5,
      "qty_stars": 3
    }
  },
  {
    "_id": {
      "$oid": "63010b3c0de1e8fdcf96bc24"
    },
    "title": "Lenovo V110-15IAP",
    "description": "Asus VivoBook 15 X540NA-GQ008T Chocolate Black, 15.6\" HD, Pentium N4200, 4GB, 500GB, Windows 10 Home, En kbd",
    "img_src": "https://webscraper.io/images/test-sites/e-commerce/items/cart2.png",
    "price": 356.49,
    "hdd": [
      "128",
      "256",
      "512"
    ],
    "rating": {
      "qty_reviews": 6,
      "qty_stars": 2
    }
  },
  {
    "_id": {
      "$oid": "63010b3c0de1e8fdcf96bc25"
    },
    "title": "Lenovo ThinkPad E31-80",
    "description": "Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home",
    "img_src": "https://webscraper.io/images/test-sites/e-commerce/items/cart2.png",
    "price": 404.23,
    "hdd": [
      "128",
      "256",
      "512"
    ],
    "rating": {
      "qty_reviews": 12,
      "qty_stars": 1
    }
  },
  {
    "_id": {
      "$oid": "63010b3c0de1e8fdcf96bc26"
    },
    "title": "Lenovo V110-15ISK",
    "description": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 8GB, 128GB SSD, Windows 10 Home",
    "img_src": "https://webscraper.io/images/test-sites/e-commerce/items/cart2.png",
    "price": 409.63,
    "hdd": [
      "128",
      "256",
      "512"
    ],
    "rating": {
      "qty_reviews": 9,
      "qty_stars": 3
    }
  },
  {
    "_id": {
      "$oid": "63010b3c0de1e8fdcf96bc27"
    },
    "title": "Lenovo V110-15ISK",
    "description": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Pro",
    "img_src": "https://webscraper.io/images/test-sites/e-commerce/items/cart2.png",
    "price": 454.73,
    "hdd": [
      "128",
      "256",
      "512"
    ],
    "rating": {
      "qty_reviews": 2,
      "qty_stars": 2
    }
  }
  {...}
]
```

### Rota POST `/scrape`

Essa rota é responsável por enviar uma ordem de raspagem de dados ao scraper.

É retornada uma mensagem, com o `orderId` que pode ser utilizado para verificar se a raspagem já foi concluída.

`STATUS CODE 201`
```json
{
  "message": "Scrape order created!",
  "order_id": "63017ec05c1c2fc9080d35d0"
}
```

### Rota GET `/scrape?orderId=<order_id>`

Essa rota é responsável por verificar o andamento da solicitação de scraping. Existe a possibilidade de dois retornos.

Raspagem de dados ainda `não` foi concluída:

`STATUS CODE 200`
```json
{
  "message": "Scraping order is not completed"
}
```

Raspagem de dados concluída:

`STATUS CODE 200`
```json
{
  "message": "Scraping order already completed"
}
```
## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
docker container exec -it webscraper_api bash -c "pytest ./tests --verbose"
```

Ao todo a aplicação possui `60%` de cobertura de testes.

Caso queira ver a cobertura de testes rode o comando

```bash
docker container exec -it webscraper_api bash -c "pytest --cov=webscraper_api tests/"
```


## Aprendizados

Aprendi a utilizar a ferramenta `Playwright` para a realização do web scraper,
além de poder ter exercitado meus conhecimentos de `Python` e construção de `APIs RESTful` utilizando `Flask`.

Pude melhorar meu conhecimento na construção de APIs providas por banco de dados não relacional, no caso o mongoDB,
principalmente utilizando o python, pois geralmente utilizo o `nodeJS` para essas tarefas. Coloquei isso como desafio pessoal.

Algo que gostei bastante foi da utilização do `Playwright` que facilita em muito o scraping, principalmente se comparar ao que utilizava.
(`parsel` + `requests`).

Algo que tive um pouco de dificuldade foi no momento de testar a aplicação, por isso não completei 100% de cobertura e parei nos 60%.
Mas foi bom pois melhorei os meus conhecimentos com o pytest, e configuração de mocks para aplicações com Flask, e me desafiei em entregar
ao menos 50% de cobertura.
