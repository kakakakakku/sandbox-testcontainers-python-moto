import os

import boto3

if os.environ['ENV'] == 'local':
    s3 = boto3.client('s3', region_name='us-east-1', endpoint_url='http://localhost:5000')
elif os.environ['ENV'] == 'test':
    s3 = boto3.client(
        's3', region_name='us-east-1', endpoint_url=f'http://localhost:{os.environ['TESTCONTAINERS_MOTO_PORT']}'
    )
else:
    s3 = boto3.client('s3', region_name='us-east-1')


class MyModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)


if __name__ == '__main__':
    model_instance = MyModel('steve', 'is awesome')
    model_instance.save()
