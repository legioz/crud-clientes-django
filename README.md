# CRUD Clientes Simples

## .env file

```sh
SECRET_KEY=django-insecure-a%a-9*2*e*m0!rcibl)u*l3kkp4*k6hini_*ndif4qg*x2d79o
DEBUG=True
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
TZ=
PGTZ=
```

## Execução do projeto em containers

1. Construção das imagens e criação dos containers

```sh
docker-compose build
```

2. Execução dos containers em background

```sh
docker-compose up -d
```

3. Pausa nos containers

```sh
docker-compose down
```

## Execução sem container com SQLite

1. Criação do virtual env  

```sh
python -m venv venv
```

2. Ativação do virtual env

```sh
source venv/bin/activate
```
3. Instalação das dependências

```sh
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

4. Execução do projeto em desenvolvimento

```sh
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```