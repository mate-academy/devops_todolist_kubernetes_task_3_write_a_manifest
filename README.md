# Django ToDo list

This is a todo list web application with basic features of most web apps, i.e., accounts/login, API, and interactive UI. To do this task, you will need:

- CSS | [Skeleton](http://getskeleton.com/)
- JS  | [jQuery](https://jquery.com/)

## Explore

Try it out by installing the requirements (the following commands work only with Python 3.8 and higher, due to Django 4):

```
pip install -r requirements.txt
```

Create a database schema:

```
python manage.py migrate
```

And then start the server (default is http://localhost:8000):

```
python manage.py runserver
```

Now you can browse the [API](http://localhost:8000/api/) or start on the [landing page](http://localhost:8000/).

## Task

# ToDo Application Setup and Deployment Guide

### 1. Fork the Repository
https://github.com/SHCHERBANV/devops_todolist_kubernetes_task_3_write_a_manifest.git
### 2. Create a Dockerfile

### 3. Modify API for Readiness and Liveness Endpoints /api/ views.py & urls.py

### 4. Build and Push Docker Image
docker build -f Dockerfile -t shcherbanvasyl499/todoapp:3.0.0 .
docker run -d -p 8080:8080 shcherbanvasyl499/todoapp:3.0.0
docker login
docker push shcherbanvasyl499/todoapp:3.0.0


### 5. Create Kubernetes Manifests

1. Create a folder named `.infrastructure` in the root of your project.
2. Create the following files in the `.infrastructure` folder:

    #### `namespace.yml`

    #### `busybox.yml`

    #### `todoapp-pod.yml`


### 6. Apply Kubernetes Manifests

1. Apply the  manifest:

    ```bash
    kubectl apply -f .infrastructure/
    ```


### 7. Test ToDo Application

#### Using Port-Forward

1. Forward the port to access the ToDo application locally:

    ```bash
    kubectl port-forward pod/todoapp-pod -n todoapp 8080:8080
    ```

2. Access the application at [http://localhost:8080](http://localhost:8080).

#### Using Busyboxplus:curl Container

1. Execute commands inside the busybox container to test the application:

    ```bash
    kubectl exec -it busybox -n todoapp -- sh
    curl http://localhost:8080/api/health   
    curl http://localhost:8080/api/ready
    ```

### 8. Create a Pull Request
