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

Create a kubernetes manifest for a pod which will containa ToDo app container:

1. Fork this repository.
1. Create a simple `Dockerfile` for the ToDo application
7. Add readiness endpoint code to `api` of the appliation (modify `api/views.py` and `api/urls.py`)
1. Add liveness endpoint cide to `api` of the application (modify `api/views.py` and `api/urls.py`)
1. Build your image and push to your personal Docker Hub account into the `todoapp` repository with the `3.0.0` tag (`todoapp:3.0.0`)
1. All manifests should be located under `.infrastructure` folder
1. Create a `manifest` which can be used to create a namespace. File should be named `namespace.yml` and should contain the following content:
```
apiVersion: v1
kind: Namespace
metadata:
 name: todoapp
```
8. Creata a pod `manifest` which will start a `busyboxplus:curl` container in a cluster. File should be named `busybox.yml`.
1. Create a pod `manifest` which will be using previously created image with tag `{yourname}/todoapp:3.0.0`. File should be named `todoapp-pod.yml`.
1. ToDo app pod `manifest` should have a readiness probe configured
1. ToDo app pod `manifest` should have a liveness probe configured
1. `README.md` file should contain instructions on how to apply all manifests
1. `README.md` file should contain instructions on how to test ToDo application using the `port-forward` command
1. `README.md` file should contain instructions on how to test application using the
`busyboxplus:curl` container
1. Create PR with your changes and attach it for validation on a platform.

### How to run
link to [image](https://hub.docker.com/layers/dsvyrydoff/todoapp/3.0.0/images/sha256-27c2511eab6fe4cf733c27b7c6e9c574ae7a2ec70456ceb0490d4d654b942105?context=repo)

To create namespace for pods run
"kubectl apply -f namespace.yml"

To create pod for todoapp run
"kubectl apply -f todoapp-pod.yml"

To create pod for busybox run
"kubectl get pods -n todoapp"

Check pods
"kubectl get pods -n todoapp"

To use port-forward run
"kubectl port-forward pod/todoapp 8081:8080 -n todoapp"

To test using busybox run
"kubectl get pods -o wide -n todoapp"
you will get app pod's IP

than run
"kubectl -n todoapp exec -it busybox -- sh"
and than
"curl <pod's IP>"
