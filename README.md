# Django ToDo list

This is a todo list web application with basic features of most web apps, i.e., accounts/login, API, and interactive UI. To do this task, you will need:

- CSS | [Skeleton](http://getskeleton.com/)
- JS | [jQuery](https://jquery.com/)

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
1. Add readiness endpoint code to `api` of the appliation (modify `api/views.py` and `api/urls.py`)
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

1. Enter directory that contains all manifest files: -`cd .\.infrastructure\`
1. To create a namespace for out project run: -`kubectl apply -f namespace.yml`
1. To run pods type 2 commands to the terminal from the root of the repo : - `kubectl apply -f todoapp-pod.yml` - `kubectl apply -f busybox.yml`
1. If there are no errors, run ``kubectl get pods -0 wide -n mateapp`
1. To test your todoapp containter run: -`kubectl -n mateapp exec -it busybox -- sh`
   Once you are inside of busybox type: -`curl<todoapp_ip>:8000`
   where `<todoapp_ip>` is ip addres of your todoapp container(you can get it using command from step 4.)
