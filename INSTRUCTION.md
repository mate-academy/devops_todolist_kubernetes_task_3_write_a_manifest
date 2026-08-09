# Instructions for Deploying and Testing ToDo Application on Kubernetes

This document provides instructions on how to build the Docker image, deploy all Kubernetes manifests, and test the ToDo application using `kubectl port-forward` and the `busyboxplus:curl` container.

---

## 1. Build and Push Docker Image

Before deploying the application to Kubernetes, build the Docker image and push it to Docker Hub:

```bash
# Build the Docker image
docker build -t b1mb4/todoapp:3.0.0 .

# Push the Docker image to Docker Hub
docker push b1mb4/todoapp:3.0.0
```

---

## 2. Apply Kubernetes Manifests

All Kubernetes manifests are located in the `.infrastructure` directory. Apply them in the following order:

```bash
# 1. Create the namespace 'todoapp'
kubectl apply -f .infrastructure/namespace.yml

# 2. Deploy the ToDo application Pod
kubectl apply -f .infrastructure/todoapp-pod.yml

# 3. Deploy the busybox Pod for testing
kubectl apply -f .infrastructure/busybox.yml
```

Or apply all manifests at once:

```bash
kubectl apply -f .infrastructure/
```

Verify that the pods are running:

```bash
kubectl get pods -n todoapp
```

---

## 3. Test the Application using `port-forward`

Forward local port `8000` to port `8000` of the `todoapp` pod:

```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Open a new terminal or browser and test the endpoints:

```bash
# Test the main landing page
curl http://localhost:8000/

# Test readiness probe endpoint
curl http://localhost:8000/api/readiness

# Test liveness probe endpoint
curl http://localhost:8000/api/liveness
```

---

## 4. Test the Application using `busyboxplus:curl` Container

To test internal cluster communication between containers in the `todoapp` namespace:

1. Obtain the IP address of the `todoapp` pod:

```bash
kubectl get pod todoapp -n todoapp -o wide
```

2. Execute `curl` commands from inside the `busybox` pod using the pod's IP address:

```bash
# Test the main application
kubectl exec -it busybox -n todoapp -- curl http://<POD_IP>:8000/

# Test the readiness endpoint
kubectl exec -it busybox -n todoapp -- curl http://<POD_IP>:8000/api/readiness

# Test the liveness endpoint
kubectl exec -it busybox -n todoapp -- curl http://<POD_IP>:8000/api/liveness
```
