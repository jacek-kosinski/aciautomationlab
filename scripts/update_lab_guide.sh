#!/usr/bin/env bash
docker stop jacekkosinski-acilabguide
docker rm jacekkosinski-acilabguide
docker pull jacekkosinski/acilabguide
docker run -d --name jacekkosinski-acilabguide -p 8080:80 jacekkosinski/acilabguide
