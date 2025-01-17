# Genealogy

## Prerequisite

```
python 3.10.8
docker 20.10.17
docker-compose 1.29.2
```

## Python Flask framework with MVC design pattern

```
Flask
Flask-SQLAlchemy -- ORM
Flask-restx -- API & Swagger
pytest -- Testing
```

## Using virtual environment

```
python3 -m venv env
. env/bin/activate
deactivate
```

## Install requirements

```
pip install -r requirements.txt
```

## Using database

```
docker-compose -f docker/mysql.yml up -d
docker-compose -f docker/mysql.yml down
```

## Start server

```
flask --app src run
```

## Test

```
pytest tests\resources\family_resource.py
pytest tests\resources\person_resource.py
pytest tests\resources\relationship_type_resource.py
```

## Contributors
