#!/bin/bash

docker build -t jup014/team-yourmove-log-api:0.2 . -f api-build.Dockerfile
docker push jup014/team-yourmove-log-api:0.2