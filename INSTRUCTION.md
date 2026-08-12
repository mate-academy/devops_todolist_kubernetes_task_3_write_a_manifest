# ToDo Application Kubernetes Deployment Instructions

## Prerequisites
- Docker installed and running
- Kubernetes cluster (Docker Desktop K8s or Minikube)
- kubectl configured
- Docker Hub account

## Step 1: Build and Push Docker Image

### Build the image
```bash
docker build . -t DRDR92/todoapp:3.0.0
```

### Login to Docker Hub
```bash
docker login -u DRDR92
```

### Push image
```bash
docker push DRDR92/todoapp:3.0.0
```

## Step 2: Deploy to Kubernetes

### Create namespace
```bash
kubectl apply -f .infrastructure/namespace.yml
```

### Create busybox pod
```bash
kubectl apply -f .infrastructure/busybox.yml
```

### Create todoapp pod
```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Verify:
```bash
kubectl get pods -n todoapp
```

## Step 3: Test

### Using port-forward
```bash
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```

Open: `http://localhost:8081/`

### Using busybox pod

Get IP:
```bash
kubectl get pods -n todoapp -o wide
```

Connect:
```bash
kubectl exec -it pod/busybox -n todoapp -- sh
```

Test:
```bash
curl http://<TODOAPP_IP>:8080/
curl http://<TODOAPP_IP>:8080/health/live
curl http://<TODOAPP_IP>:8080/health/ready
```

Exit:
```bash
exit
```

## Cleanup
```bash
kubectl delete namespace todoapp
```
