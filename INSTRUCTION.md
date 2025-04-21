# Apply Kubernetes Manifests

```sh
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

# Port-Forward to Access the App Locally

```sh
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```

#

```sh
curl http://localhost:8000/health
curl http://localhost:8000/ready
```

# Test Health & Readiness with busybox Pod

```sh
kubectl exec -it busybox -n todoapp -- /bin/sh
curl http://todoapp:8000/health
curl http://todoapp:8000/ready
```
