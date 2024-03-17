# Transcript api

## Table of Contents

1. [Dependencies](#dependencies)
2. [Getting Started](#getting-started)
3. [Commands](#commands)
4. [Development](#development)
5. [Testing](#testing)
6. [Lint](#lint)
7. [Swagger](#swagger)
8. [MessageBroker](#MessageBroker)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone  
$ cd chatbot
```


To use as a Api to do the following changes in docker-compose.yml 

```bash
# main.py for http server 
command: python app/main.py
```


If everything works, you should see the available routes [here](http://127.0.0.1:3000/spec).

The API runs locally on docker containers. You can easily change the python version you are willing to use in docker-compose.yml, by fetching a docker image of the python version you want.

## Commands

## Docker commands 
1. To build the docker image
```bash
  docker build -t chatbot-api .
```
2. To run the container 
```bash
  docker run -p 3000:3000 chatbot-api
```

## Running Python's PDB debugger with Docker
1. Add to docker-compose.yml
  ```bash
  stdin_open: true  
  tty: true 
  ```
  to the service configuration in docker-compose.yml . 
2. To debug add
   ```bash
   import pdb;pdb.set_trace();
   ```
3. The debugger is running inside the container, so we need to attach into the container to use it.

    Find the container id using 
    ```bash 
    docker container ps
    ``` 
    Use the command 
    ```bash
    docker attach <CONTAINER_ID> 
    ```
    to attach to the container.

4. Now just navigate to the page and the debugger will start, so you will be able to use the usual commands like n or c.
5. To exit you should use CONTROL + P, CONTROL + Q.
6. If you use Control + C the container will stop.
For reference click [here](https://blog.lucasferreira.org/howto/2017/06/03/running-pdb-with-docker-and-gunicorn.html/).
```
