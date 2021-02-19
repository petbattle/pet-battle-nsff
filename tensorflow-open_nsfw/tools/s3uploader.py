#!/bin/python
from minio import Minio
from minio.error import ResponseError
import os
import os.path

# https://docs.min.io/docs/python-client-api-reference.html

def deploy_model(model_name):
    #minioClient = Minio('127.0.0.1:9000',
    #                  access_key='minioadmin',
    #                  secret_key='minioadmin',
    #                 secure=False)
    minioClient = Minio(os.environ.get('MINIO_SERVICE_HOST'),
                      access_key=os.environ.get('MINIO_ACCESS_KEY'),
                      secret_key=os.environ.get('MINIO_SECRET_KEY'),
                      secure=False)

    files = []
    folder_name = model_name
    for r, d, f in os.walk(folder_name):
        for file in f:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)
        minioClient.fput_object(bucket_name='models', object_name=f , file_path='./' + f)

deploy_model("saved_model")