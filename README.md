## AI agent for Zania

### Run the following commands to start a local instance of elastic search
- ```sudo snap install docker```
- ```chmod 666 /var/run/docker.sock```
- ```docker run --memory="2g" -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.http.ssl.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.12.1```

Then run:
- ```chmod +x run.sh```
- ```(export $(cat .env | xargs) && ./run.sh)```

An example .env file is included. The run.sh script will start the service. 
