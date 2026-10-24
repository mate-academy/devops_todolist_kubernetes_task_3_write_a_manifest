# ToDo App — Kubernetes Deployment Instructions

## Prerequisites
- `kubectl` installed and configured
- Docker image `dmytro0908/todoapp:3.0.0` pushed to Docker Hub

## Apply manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml