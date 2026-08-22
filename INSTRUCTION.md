# ToDo App - Deployment Instructions

## 1. Apply all manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Verify pods are running:

```bash
kubectl get pods -n todoapp
```

## 2. Test the application via port-forward

Forward the pod's port to your local machine:

```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Then open a browser or use curl:

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/ready/
curl http://localhost:8000/api/health/
```

## 3. Test using the busybox curl container

Get the todoapp pod IP:

```bash
TODOAPP_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
```

Exec into the busybox pod and curl the todoapp pod by its IP:

```bash
kubectl exec busybox-curl -n todoapp -- sh -c "curl http://${TODOAPP_IP}:8000/api/ready/"
kubectl exec busybox-curl -n todoapp -- sh -c "curl http://${TODOAPP_IP}:8000/api/health/"
```
