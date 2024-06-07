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

1. `README.md` file should contain instructions on how to apply all manifests
1. `README.md` file should contain instructions on how to test ToDo application using the `port-forward` command
1. `README.md` file should contain instructions on how to test application using the
   `busyboxplus:curl` container
1. Create PR with your changes and attach it for validation on a platform.

1. Apply manifests by commands
   `kubectl apply -f ./.infrastructure/namespace.yml`
   `kubectl apply -f ./.infrastructure/busybox.yml`
   `kubectl apply -f ./.infrastructure/todoapp-pod.yml`

1. Port-forwarding
   run `kubectl port-forward pod/todoapp-pod 8081:8080 -n todoapp`
   visit `http://0.0.0.0:8081/api/health/`
   visit `http://0.0.0.0:8081/api/ready/` after ~ 40s refresh page to get updated status

1. Test app via curl
   get todoapp-pod ip `kubectl get pods -n todoapp -o wide`
   open todo app in interactive mode `kubectl -n todoapp exec -it curlpod -- sh`
   make a request `curl [ip from step 1]:8080/api/health/`
   make a request `curl [ip from step 1]:8080/api/ready/` after ~ 40s make another request to get updated status
