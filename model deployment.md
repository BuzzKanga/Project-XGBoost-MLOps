# Docker Container

In order to be able to deploy the model easily, it needs to be installed in a docker container.

The prediction functionality of the best model was changed so that it could receive a request containing a customer's details and would respond with a prediction whether that customer woud churn.

Initially this program [xgboost.ipynb](deployment/xgboost.ipynb) was made to work on flask and then on gunicorn.


The final version of the program [xgb_predict.py](deployment/xgb_predict.py) was the installed in a docker container using [Dockerfile](deployment/Dockerfile) and the port of the docker container (9696) set as the entry point and mapped to the server's port 9696.

The commands to build and rund the docker container are as follows:

- build from Dockerfile in current directory, add tag = project-xgboost-mlops:
  `docker build -t project-xgboost-mlops`

- run docker image created (:latest is optional)
  `docker run -it --rm --entrypoint=bash project-xgboost-mlops:latest`

- run docker with entrypoint specified in Docker file
  `docker run -it --rm  project-xgboost-mlops`

- map port on container to port on machine using -p
  `docker run -it --rm -p 9696:9696 project-xgboost-mlops`






