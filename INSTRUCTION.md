# ToDo Application — Kubernetes Deployment Instructions

## Prerequisites

- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed and configured
- A running Kubernetes cluster (e.g. Docker Desktop, Minikube, or a cloud cluster)
- Docker installed (for building and pushing the image)

---

## 1. Build & Push the Docker Image

```bash
# Build the image
docker build . -t aleksandra2402/todoapp:3.0.0

# Log in to Docker Hub
docker login -u aleksandra2402

# Push to Docker Hub
docker push aleksandra2402/todoapp:3.0.0
```

> Replace `aleksandra2402` with your Docker Hub username in both the command above and in `.infrastructure/todoapp-pod.yml`.

---

## 2. Apply All Manifests

Apply the manifests in order — namespace first, then the pods.

```bash
# 1. Create the namespace
kubectl apply -f .infrastructure/namespace.yml

# 2. Deploy the busybox helper pod
kubectl apply -f .infrastructure/busybox.yml

# 3. Deploy the ToDo application pod
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Verify everything is running:

```bash
kubectl get pods -n todoapp
```

You should see output like:

```
NAME       READY   STATUS    RESTARTS   AGE
busybox    1/1     Running   0          30s
todoapp    1/1     Running   0          30s
```

> Note: `todoapp` may show `0/1` for ~30 seconds while the readiness probe completes its startup period.

---

## 3. Test the Application via `port-forward`

Forward a local port to the todoapp pod:

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

Then open your browser or use curl:

```bash
# Main app
curl http://localhost:8080/

# Liveness probe
curl http://localhost:8080/api/health/

# Readiness probe
curl http://localhost:8080/api/ready/

# List tasks
curl http://localhost:8080/api/tasks/

# Create a task
curl -X POST http://localhost:8080/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task"}'
```

---

## 4. Test the Application via `busyboxplus:curl`

First, get the IP address of the todoapp pod:

```bash
kubectl get pods -n todoapp -o wide
```

Note the `IP` column value for the `todoapp` pod (e.g. `10.1.0.5`).

Then exec into the busybox container:

```bash
kubectl -n todoapp exec -it busybox -- sh
```

Inside the container, run curl against the todoapp pod IP:

```bash
# Replace 10.1.0.5 with the actual pod IP from the previous step

# Test main endpoint
curl 10.1.0.5:8080/

# Test liveness probe
curl 10.1.0.5:8080/api/health/

# Test readiness probe
curl 10.1.0.5:8080/api/ready/

# List tasks
curl 10.1.0.5:8080/api/tasks/

# Create a task
curl -X POST 10.1.0.5:8080/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task"}'
```

Exit the busybox shell when done:

```bash
exit
```

---

## 5. Cleanup

To remove all created resources:

```bash
kubectl delete -f .infrastructure/todoapp-pod.yml
kubectl delete -f .infrastructure/busybox.yml
kubectl delete -f .infrastructure/namespace.yml
```