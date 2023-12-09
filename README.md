# Asynchronous Tasks with FastAPI and Celery

Example of how to handle background processes with FastAPI, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost:8004](http://localhost:8004) to view the app or to [http://localhost:5556](http://localhost:5556) to view the Flower dashboard.

Trigger a new task:

```sh
$ curl http://localhost:8004/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```

Check the status:

```sh
$ curl http://localhost:8004/tasks/<TASK_ID>
```


https://gist.github.com/harshavardhana/f05b60fe6f96803743f38bea4b565bbf
https://github.com/minio/mc#add-a-cloud-storage-service

docker run -it --entrypoint=/bin/sh minio/mc
mc alias set minio http://192.168.1.92:9000 minio minio12345
mc anonymous set download minio/fastapi-celery