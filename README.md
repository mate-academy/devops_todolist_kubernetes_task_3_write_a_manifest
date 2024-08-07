Make sure you have docker installed.

Pull docker app image:

```angular2html
   docker pull sserkov84/todoapp:latest
```

Create a database schema:
Apply manifests:

```angular2html
kubectl apply -f .infrastructure/namespace.yml
```
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```
```
kubectl apply -f .infrastructure/busybox.yml
```

Use this command to see logs:
```
python manage.py runserver
```angular2html
kubectl logs todoapp -n todoapp
```

Use following command to test api using port-forward:
```angular2html
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```
 Use following commant to connect busybox:
```angular2html
kubectl -n todoapp exec -it busybox -- sh
```
```angular2html
curl http://todoapp-pod:8080
```

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
8. Creata a pod `manifest` which will start a `ikulyk404/busyboxplus:curl` container in a cluster. File should be named `busybox.yml`.
1. Create a pod `manifest` which will be using previously created image with tag `{yourname}/todoapp:3.0.0`. File should be named `todoapp-pod.yml`.
1. ToDo app pod `manifest` should have a readiness probe configured
1. ToDo app pod `manifest` should have a liveness probe configured
1. `README.md` file should contain instructions on how to apply all manifests
1. `README.md` file should contain instructions on how to test ToDo application using the `port-forward` command
1. `README.md` file should contain instructions on how to test application using the
`busyboxplus:curl` container
1. Create PR with your changes and attach it for validation on a platform.
