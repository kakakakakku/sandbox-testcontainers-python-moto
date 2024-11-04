# sandbox-testcontainers-python-moto

## Format & Lint

```sh
$ uvx ruff format
$ uvx ruff check --fix
```

## Run local

```sh
$ docker run --rm -p 5000:5000 --name moto motoserver/moto:latest
$ aws s3api create-bucket --bucket mybucket --region us-east-1 --endpoint-url=http://localhost:5000
$ ENV=local uv run src/mymodel.py
```

## Run test

```sh
$ ENV=test uv run pytest -p no:warnings --verbose tests
```
