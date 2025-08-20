# 🖥️ Elasticsearch & Kibana Setup Guide

## Installation (Docker)
```bash
docker network create elastic

docker pull docker.elastic.co/elasticsearch/elasticsearch:8.6.0
docker run -d --name es01 --net elastic -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.6.0

docker pull docker.elastic.co/kibana/kibana:8.6.0
docker run -d --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.6.0
