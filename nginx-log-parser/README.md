# NGINX Log Generator Docker Setup & Log Monitoring

This guide explains how to:
- Build a Docker image for the nginx-log-generator using kscarlett/nginx-log-generator and alpine:latest as the base image.
- Run a Python script to monitor logs for non-200 responses
- Stream container logs to your local `/var/log/nginx/access.log` continuously.
---

## 1. Build the Docker Image

    docker build -t custom-nginx-logger:alpine .

## 2. Run the Docker container
  
    docker run -d custom-nginx-logger:alpine --name custom-nginx-logger

## 3. Stream container logs to /var/log/nginx/access.logs

    docker logs -f custom-nginx-logger > /var/log/nginx/access.log  #requires sudo

kscarlett/nginx-log-generator prints out the fake logs into stdout and does not have a request handler. This is an intuitive way.

## 4. Run the log-monitor.py script

    python3 log-monitor.py
