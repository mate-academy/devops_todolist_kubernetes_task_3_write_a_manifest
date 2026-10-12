# ToDo app Kubernetes instructions

## Build and publish the image

From the repository root, build and push the image to Docker Hub:

```sh
docker build -t rimbozero/todoapp:3.0.0 .
docker push rimbozero/todoapp:3.0.0
```

Authenticate with Docker Hub using `docker login` if needed.

## Apply the manifests

Create the namespace first, then create both pods:

```sh
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/todoapp-service.yml
kubectl apply -f .infrastructure/busybox.yml
```

Check pod status and wait for the ToDo pod to become ready:

```sh
kubectl get pods -n todoapp
kubectl wait --for=condition=Ready pod/todoapp -n todoapp --timeout=120s
```

## Test with port-forward

Forward local port 8000 to the ToDo pod:

```sh
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

In another terminal, test the application and its health endpoints:

```sh
curl http://localhost:8000/
curl http://localhost:8000/api/ready/
curl http://localhost:8000/api/live/
```

## Test from the busyboxplus:curl pod

Exec into the busybox pod and call the ToDo pod by its DNS name:

```sh
kubectl exec -it busybox -n todoapp -- sh
curl http://todoapp:8000/
curl http://todoapp:8000/api/ready/
curl http://todoapp:8000/api/live/
```

The pod name resolves as `todoapp` within the `todoapp` namespace.
