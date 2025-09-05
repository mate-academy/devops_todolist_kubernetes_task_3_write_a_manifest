# Build & Run Instructions

## Build the image locally
```
docker build -t {username}/todoapp:3.0.0 .
```

## Push to Docker Hub

```
docker push {username}/todoapp:3.0.0
```

## Create namespace

```bash
kubectl apply -f .infrastructure/namespace.yml
```

## Apply todoapp and busybox

```bash
kubectl apply -f .infrastructure/ -n todoapp
````

# Testing

## The simplest way is to obtain the namespaces and monitor their readiness status

```bash
kubectl get pods -n todoapp -w
```
todoapp should be ready in about 30 seconds

## Forward ports to access application
```bash
kubectl port-forward pod/todoapp 8081:8080
```

## Get todo app pod ip address

```bash
kubectl get pod todoapp -n todoapp -o wide
```

## Connect to the busybox pod to access endpoints

```bash
kubectl -n todoapp exec -it busybox -- sh
```
