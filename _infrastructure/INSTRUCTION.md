# How to apply manifests and test the Todo app

## 1. Create namespace and pods

```bash
# Apply namespace
kubectl apply -f _infrastructure/namespace.yml

# Apply busybox pod
kubectl apply -f _infrastructure/busybox.yml

# Apply todoapp pod
kubectl apply -f _infrastructure/todoapp-pod.yml

# Check that pods are running
kubectl get pods -n todoapp

# Redirect traffic from one or more local ports to a sub
kubectl -n todoapp port-forward pod/todoapp 8000:8000

# Test busyboxplus:curl container
docker build -f Dockerfile.busyboxpluscurl   -t mcisb/busyboxplus:curl .
docker push mcisb/busyboxplus:curl

# Call health endpoint of todoapp from the running busybox pod
kubectl -n todoapp exec busybox -- curl -sS http://todoapp:8000/api/health/ready/
kubectl -n todoapp exec busybox -- curl -sS http://todoapp:8000/api/health/live/
