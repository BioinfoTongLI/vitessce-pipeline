#! /bin/sh
VERSION=0.3.2

docker build --platform=linux/amd64 -t haniffalab/webatlas-pipeline:${VERSION} -f ./Dockerfile .
docker build --platform=linux/amd64 -t haniffalab/webatlas-pipeline-build_config:${VERSION} -f ./Dockerfile.build_config .
