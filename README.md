# sandbox-testcontainers-python-moto

![badge.svg](https://github.com/kakakakakku/sandbox-testcontainers-python-moto/actions/workflows/pytest.yml/badge.svg)

Sandbox for pytest using [Testcontainers for Python](https://github.com/testcontainers/testcontainers-python) and [Moto](https://github.com/getmoto/moto).

## Format & Lint

```sh
$ uvx ruff format
$ uvx ruff check --fix
```

## Run local

```sh
# Run Moto
$ docker run --rm -p 5000:5000 --name moto motoserver/moto:latest

# Create Amazon S3 Bucket
$ aws s3api create-bucket --bucket mybucket --region us-east-1 --endpoint-url=http://localhost:5000

# Run local
$ ENV=local uv run src/mymodel.py

# Check Amazon S3 Object
$ aws s3 ls mybucket --region us-east-1 --endpoint-url=http://localhost:5000
2024-11-05 20:00:00         10 steve
```

## Run test

```sh
# Run test
$ ENV=test uv run pytest -p no:warnings --verbose tests
```
