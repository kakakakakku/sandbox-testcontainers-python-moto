import os

import boto3
import pytest
from testcontainers.core.container import DockerContainer


@pytest.fixture(scope='module', autouse=True)
def _setup():
    with DockerContainer('motoserver/moto').with_exposed_ports(5000) as container:
        os.environ['TESTCONTAINERS_MOTO_PORT'] = container.get_exposed_port(5000)

        s3 = boto3.client(
            's3', region_name='us-east-1', endpoint_url=f'http://localhost:{os.environ['TESTCONTAINERS_MOTO_PORT']}'
        )
        s3.create_bucket(Bucket='mybucket')

        yield


def test_my_model_save():
    from mymodel import MyModel, s3

    model_instance = MyModel('steve', 'is awesome')
    model_instance.save()

    body = s3.get_object(Bucket='mybucket', Key='steve')['Body'].read().decode('utf-8')

    assert body == 'is awesome'
