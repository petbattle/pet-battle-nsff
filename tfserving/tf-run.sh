#!/bin/bash

export AWS_ACCESS_KEY_ID=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
export S3_HOST=127.0.0.1:9000

podman run -d --name tfserving --net host \
    -p 8500:8500 \
    -p 8501:8501 \
    -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
    -e AWS_REGION=us-east-1 -e S3_REGION=us-east-1 \
    -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
    -e S3_ENDPOINT=${S3_HOST} -e S3_LOCATION=${S3_HOST} -e S3_USE_HTTPS="0" -e S3_VERIFY_SSL=false -e S3_VERIFY_SSL="0" \
    tensorflow/serving \
    --model_config_file=s3://models/models.config \
    --monitoring_config_file=s3://models/prometheus_config.config \
    --model_config_file_poll_wait_seconds=300 \
    --rest_api_timeout_in_ms=30000
