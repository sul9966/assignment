# Coding Assessment

The assessment has 3 files. 
1. main.py  -- Python script used to call the rest api and get macaddress.
2. requiement.txt -- used to download python request library
3. Dockerfile  -- Dockerfile to build a container image.

Build Docker Image using command

`Docker build -t imageName .`

Run Docker Container using command. You will need to pass apikey and macaddress to get the results.

`Docker run --rm imageName apikey macaddress`

## Using Secrets
* Secrets like API key can be passed as an argument to the docker command. Not storing secret in the image/repository is one simple/basic security measure. 
* secrets can also be stored as environment variables. 
* If its a kubernetes environment. Secrets can be created in the Kubernetes environment that can be mapped to pods. 


